# Graph Database Query Exploration

## Overview

This notebook explores the use of graph databases, specifically Neo4j, to visualize and analyze relationships in a movie review dataset. Two queries were executed to understand the connections between actors, movies, and genres.

## Learnings

### 1. Understanding Graph Databases
- **Nodes and Relationships:** 
  - Nodes represent entities (e.g., Movies, Persons, Genres).
  - Relationships define how these nodes are connected (e.g., `ACTED_IN`, `IN_GENRE`).

### 2. Neo4j Cypher Queries
- **Basic Query Structure:**
  - `MATCH` is used to define the pattern you are looking for.
  - `RETURN` specifies what you want to retrieve.
  - `LIMIT` is used to constrain the number of results.

- **Examples:**
  - **Query 1:** `MATCH p=()-[:ACTED_IN]->() RETURN p LIMIT 25;`
    - **Objective:** Retrieve and visualize up to 25 actor-movie relationships.
    - **Visualization:** Displays the relationships between various movies and actors.

  - **Query 2:** `MATCH p=()-[:IN_GENRE]->() RETURN p LIMIT 25;`
    - **Objective:** Retrieve and visualize up to 25 movie-genre relationships.
    - **Visualization:** Displays how different movies are categorized under various genres.

### 3. Visualization Interpretation
- The visualizations provided by Neo4j show a graph structure where:
  - **Green Nodes** represent movies.
  - **Brown/Blue Nodes** represent actors/genres.
  - **Edges** represent the relationships between these entities (e.g., `ACTED_IN`, `IN_GENRE`).

## Files
- **QA_GraphDB.ipynb:** The Jupyter notebook used to run the Neo4j queries and analyze the graph data.
- **Demo1.png:** Visualization of the actor-movie relationships (`ACTED_IN`).
- **Demo2.png:** Visualization of the movie-genre relationships (`IN_GENRE`).
