#!/usr/bin/env python3
"""
Semantic Scholar MCP Server - Streamable HTTP Transport
A Model Context Protocol (MCP) server for accessing Semantic Scholar's academic database.
Implements the MCP Streamable HTTP transport protocol.
"""

import asyncio
import logging
import os
from typing import Any, Dict, List, Optional

from mcp.server import FastMCP
from pydantic import BaseModel, Field

from search import (
    search_papers, get_paper_details, get_author_details, get_citations_and_references,
    search_authors, search_paper_match, get_paper_autocomplete, get_papers_batch,
    get_authors_batch, search_snippets, get_paper_recommendations_from_lists,
    get_paper_recommendations
)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize the FastMCP server
host = os.getenv("HOST", "0.0.0.0")
port = int(os.getenv("PORT", "3000"))
app = FastMCP("Semantic Scholar MCP Server", host=host, port=port)

# Tool implementations
@app.tool()
async def search_semantic_scholar_papers(
    query: str,
    num_results: int = 10
) -> List[Dict[str, Any]]:
    """
    Search for papers on Semantic Scholar using a query string.
    
    Args:
        query: Search query for papers
        num_results: Number of results to return (max 100)
    
    Returns:
        List of paper objects with details like title, authors, year, abstract, etc.
    """
    logger.info(f"Searching for papers with query: {query}, num_results: {num_results}")
    try:
        results = await asyncio.to_thread(search_papers, query, num_results)
        return results
    except Exception as e:
        logger.error(f"Error searching papers: {e}")
        raise Exception(f"An error occurred while searching: {str(e)}")

@app.tool()
async def get_semantic_scholar_paper_details(
    paper_id: str
) -> Dict[str, Any]:
    """
    Get details of a specific paper on Semantic Scholar.
    
    Args:
        paper_id: Paper ID (e.g., Semantic Scholar paper ID or DOI)
    
    Returns:
        Paper object with comprehensive details
    """
    logger.info(f"Fetching paper details for paper ID: {paper_id}")
    try:
        paper = await asyncio.to_thread(get_paper_details, paper_id)
        return paper
    except Exception as e:
        logger.error(f"Error fetching paper details: {e}")
        raise Exception(f"An error occurred while fetching paper details: {str(e)}")

@app.tool()
async def get_semantic_scholar_author_details(
    author_id: str
) -> Dict[str, Any]:
    """
    Get details of a specific author on Semantic Scholar.
    
    Args:
        author_id: Author ID (Semantic Scholar author ID)
    
    Returns:
        Author object with comprehensive details including publications, h-index, etc.
    """
    logger.info(f"Fetching author details for author ID: {author_id}")
    try:
        author = await asyncio.to_thread(get_author_details, author_id)
        return author
    except Exception as e:
        logger.error(f"Error fetching author details: {e}")
        raise Exception(f"An error occurred while fetching author details: {str(e)}")

@app.tool()
async def get_semantic_scholar_citations_and_references(
    paper_id: str
) -> Dict[str, Any]:
    """
    Get citations and references for a specific paper on Semantic Scholar.
    
    Args:
        paper_id: Paper ID to get citations and references for
    
    Returns:
        Object containing citations and references lists
    """
    logger.info(f"Fetching citations and references for paper ID: {paper_id}")
    try:
        citations_refs = await asyncio.to_thread(get_citations_and_references, paper_id)
        return citations_refs
    except Exception as e:
        logger.error(f"Error fetching citations and references: {e}")
        raise Exception(f"An error occurred while fetching citations and references: {str(e)}")

@app.tool()
async def search_semantic_scholar_authors(
    query: str,
    limit: int = 10
) -> List[Dict[str, Any]]:
    """
    Search for authors on Semantic Scholar using a query string.
    
    Args:
        query: Search query for authors
        limit: Maximum number of authors to return
    
    Returns:
        List of author objects with details
    """
    logger.info(f"Searching for authors with query: {query}, limit: {limit}")
    try:
        results = await asyncio.to_thread(search_authors, query, limit)
        return results
    except Exception as e:
        logger.error(f"Error searching authors: {e}")
        raise Exception(f"An error occurred while searching authors: {str(e)}")

@app.tool()
async def get_semantic_scholar_paper_match(
    query: str
) -> Dict[str, Any]:
    """
    Find the best matching paper on Semantic Scholar using title-based search.
    
    Args:
        query: Paper title or description to match
    
    Returns:
        Best matching paper object
    """
    logger.info(f"Finding paper match for query: {query}")
    try:
        result = await asyncio.to_thread(search_paper_match, query)
        return result
    except Exception as e:
        logger.error(f"Error finding paper match: {e}")
        raise Exception(f"An error occurred while finding paper match: {str(e)}")

@app.tool()
async def get_semantic_scholar_paper_autocomplete(
    query: str
) -> List[str]:
    """
    Get paper title autocompletion suggestions for a partial query.
    
    Args:
        query: Partial paper title for autocomplete suggestions
    
    Returns:
        List of autocomplete suggestions
    """
    logger.info(f"Getting paper autocomplete for query: {query}")
    try:
        results = await asyncio.to_thread(get_paper_autocomplete, query)
        return results
    except Exception as e:
        logger.error(f"Error getting autocomplete suggestions: {e}")
        raise Exception(f"An error occurred while getting autocomplete suggestions: {str(e)}")

@app.tool()
async def get_semantic_scholar_papers_batch(
    paper_ids: List[str]
) -> List[Dict[str, Any]]:
    """
    Get details for multiple papers at once using batch API.
    
    Args:
        paper_ids: List of paper IDs to fetch
    
    Returns:
        List of paper objects
    """
    logger.info(f"Fetching batch paper details for {len(paper_ids)} papers")
    try:
        results = await asyncio.to_thread(get_papers_batch, paper_ids)
        return results
    except Exception as e:
        logger.error(f"Error fetching batch paper details: {e}")
        raise Exception(f"An error occurred while fetching batch paper details: {str(e)}")

@app.tool()
async def get_semantic_scholar_authors_batch(
    author_ids: List[str]
) -> List[Dict[str, Any]]:
    """
    Get details for multiple authors at once using batch API.
    
    Args:
        author_ids: List of author IDs to fetch
    
    Returns:
        List of author objects
    """
    logger.info(f"Fetching batch author details for {len(author_ids)} authors")
    try:
        results = await asyncio.to_thread(get_authors_batch, author_ids)
        return results
    except Exception as e:
        logger.error(f"Error fetching batch author details: {e}")
        raise Exception(f"An error occurred while fetching batch author details: {str(e)}")

@app.tool()
async def search_semantic_scholar_snippets(
    query: str,
    limit: int = 10
) -> List[Dict[str, Any]]:
    """
    Search for text snippets from papers that match the query.
    
    Args:
        query: Search query for text snippets within papers
        limit: Maximum number of snippets to return
    
    Returns:
        List of snippet objects with context and source paper information
    """
    logger.info(f"Searching for text snippets with query: {query}, limit: {limit}")
    try:
        results = await asyncio.to_thread(search_snippets, query, limit)
        return results
    except Exception as e:
        logger.error(f"Error searching snippets: {e}")
        raise Exception(f"An error occurred while searching snippets: {str(e)}")

@app.tool()
async def get_semantic_scholar_paper_recommendations_from_lists(
    positive_paper_ids: List[str],
    negative_paper_ids: List[str] = [],
    limit: int = 10
) -> List[Dict[str, Any]]:
    """
    Get recommended papers based on lists of positive and negative example papers.
    
    Args:
        positive_paper_ids: List of positive example paper IDs
        negative_paper_ids: List of negative example paper IDs
        limit: Maximum number of recommendations to return
    
    Returns:
        List of recommended paper objects with relevance scores
    """
    logger.info(f"Getting paper recommendations from lists: {len(positive_paper_ids)} positive, {len(negative_paper_ids)} negative, limit: {limit}")
    try:
        results = await asyncio.to_thread(get_paper_recommendations_from_lists, positive_paper_ids, negative_paper_ids or [], limit)
        return results
    except Exception as e:
        logger.error(f"Error getting paper recommendations from lists: {e}")
        raise Exception(f"An error occurred while getting paper recommendations from lists: {str(e)}")

@app.tool()
async def get_semantic_scholar_paper_recommendations(
    paper_id: str,
    limit: int = 10
) -> List[Dict[str, Any]]:
    """
    Get recommended papers for a single positive example paper.
    
    Args:
        paper_id: Paper ID to get recommendations for
        limit: Maximum number of recommendations to return
    
    Returns:
        List of recommended paper objects with relevance scores
    """
    logger.info(f"Getting paper recommendations for single paper: {paper_id}, limit: {limit}")
    try:
        results = await asyncio.to_thread(get_paper_recommendations, paper_id, limit)
        return results
    except Exception as e:
        logger.error(f"Error getting paper recommendations for single paper: {e}")
        raise Exception(f"An error occurred while getting paper recommendations for single paper: {str(e)}")

if __name__ == "__main__":
    logger.info(f"Starting Semantic Scholar MCP HTTP Server on {host}:{port}")
    
    # Run the FastMCP server with streamable HTTP transport
    app.run(transport="streamable-http")
