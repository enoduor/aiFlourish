-- Table: category
CREATE TABLE category (
    id SERIAL PRIMARY KEY,              -- Auto-incrementing ID field (Primary Key)
    name VARCHAR(100) UNIQUE NOT NULL   -- Name of the category with a max length of 100 characters (Unique)
);

-- Table: ai_tool (formerly stuffs)
CREATE TABLE aiTool (
    id SERIAL PRIMARY KEY,              -- Auto-incrementing ID field (Primary Key)
    name_of_tool TEXT NOT NULL,         -- Tool name (Required field)
    description TEXT,                   -- Description (Optional field)
    tutorial_tool TEXT,                 -- Tutorial tool (Optional field)
    ad TEXT DEFAULT NULL,               -- Ad (Optional, with a default value of NULL)
    youtube_link TEXT,                  -- YouTube link (Optional field)
    website_link VARCHAR(200) DEFAULT NULL  -- Website link (URLField with NULL allowed)
);

-- Many-to-Many relationship table for ai_tool and category
CREATE TABLE aiToolCategories (
    id SERIAL PRIMARY KEY,              -- Auto-incrementing ID field (Primary Key)
    ai_tool_id INTEGER NOT NULL,        -- Foreign Key referencing ai_tool
    category_id INTEGER NOT NULL,       -- Foreign Key referencing category
    CONSTRAINT fk_ai_tool FOREIGN KEY (ai_tool_id) REFERENCES ai_tool (id) ON DELETE CASCADE,
    CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES category (id) ON DELETE CASCADE,
    UNIQUE(ai_tool_id, category_id)     -- Unique constraint to avoid duplicate category assignments for a tool
);
