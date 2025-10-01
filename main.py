from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.agent.agentic_workflow import GraphBuilder
from src.logger import logger
from src.exception import CustomException
import os

app = FastAPI(title="AI Travel Agent API", version="1.0")


class QueryRequest(BaseModel):
    """
    Request schema for travel agent queries.
    """
    query: str


@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    """
    Endpoint for querying the AI Travel Agent.

    Parameters
    ----------
    query : QueryRequest
        The user query containing a travel-related question.

    Returns
    -------
    dict
        The agent's response containing a detailed travel plan.
    """
    try:
        logger.info(f"Received travel query: {query.query}")

        # Initialize agent workflow
        graph = GraphBuilder()
        travel_agent = graph()

        # Optional: Save execution graph for debugging/visualization
        try:
            if not os.path.exists("graph.png"):
                png_graph = travel_agent.get_graph().draw_mermaid_png()
                with open("graph.png", "wb") as f:
                    f.write(png_graph)
                logger.info("Execution graph saved as graph.png")
            else:
                logger.info("Execution graph already exists, skipping save.")
        except Exception as e:
            logger.warning(f"Failed to save execution graph: {e}")

        # Run query through the agent
        output = travel_agent.invoke({"messages": [query.query]})
        logger.debug(f"Raw agent output: {output}")

        # Extract final response
        if isinstance(output, dict) and "messages" in output:
            last_message = output["messages"][-1]
            final_output = getattr(last_message, "content", str(last_message))
        else:
            final_output = str(output)

        logger.info("Travel query processed successfully.")
        return {"answer": final_output}

    except CustomException as ce:
        logger.error(f"Custom exception encountered: {ce}")
        raise HTTPException(status_code=500, detail=str(ce))

    except Exception as e:
        logger.exception("Unexpected error in /query endpoint.")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, timeout_keep_alive=120)