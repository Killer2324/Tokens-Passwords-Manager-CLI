instruction = """
    CREATE TABLE IF NOT EXISTS api_key (
        id int(255) auto_increment not null,
        name varchar(255) not null,
        content TEXT not null,
        created_at datetime not null,
        CONSTRAINT pk_keys PRIMARY KEY(id)
    );
"""