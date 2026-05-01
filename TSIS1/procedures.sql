-- ============================================================
--  PhoneBook Stored Procedures & Functions  (TSIS 1)
--  New objects only — does NOT duplicate Practice 7/8 objects.
-- ============================================================


-- ------------------------------------------------------------
-- 3.4 a)  add_phone
--   Adds a new phone number to an existing contact (by name).
-- ------------------------------------------------------------
CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone        VARCHAR,
    p_type         VARCHAR DEFAULT 'mobile'
)
LANGUAGE plpgsql AS $$
DECLARE
    v_id INTEGER;
BEGIN
    -- Validate phone type
    IF p_type NOT IN ('home', 'work', 'mobile') THEN
        RAISE EXCEPTION 'Invalid phone type "%". Use home, work or mobile.', p_type;
    END IF;

    SELECT id INTO v_id FROM contacts WHERE name = p_contact_name LIMIT 1;

    IF v_id IS NULL THEN
        RAISE EXCEPTION 'Contact "%" not found.', p_contact_name;
    END IF;

    -- Avoid exact duplicate (same number + type) for this contact
    IF EXISTS (
        SELECT 1 FROM phones
        WHERE contact_id = v_id AND phone = p_phone AND type = p_type
    ) THEN
        RAISE NOTICE 'Phone "%" (%) already exists for contact "%".', p_phone, p_type, p_contact_name;
        RETURN;
    END IF;

    INSERT INTO phones (contact_id, phone, type)
    VALUES (v_id, p_phone, p_type);

    RAISE NOTICE 'Phone "%" (%) added to contact "%".', p_phone, p_type, p_contact_name;
END;
$$;


-- ------------------------------------------------------------
-- 3.4 b)  move_to_group
--   Moves a contact to a group; creates the group if missing.
-- ------------------------------------------------------------
CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name   VARCHAR
)
LANGUAGE plpgsql AS $$
DECLARE
    v_contact_id INTEGER;
    v_group_id   INTEGER;
BEGIN
    -- Find contact
    SELECT id INTO v_contact_id FROM contacts WHERE name = p_contact_name LIMIT 1;
    IF v_contact_id IS NULL THEN
        RAISE EXCEPTION 'Contact "%" not found.', p_contact_name;
    END IF;

    -- Find or create group
    SELECT id INTO v_group_id FROM groups WHERE name = p_group_name LIMIT 1;
    IF v_group_id IS NULL THEN
        INSERT INTO groups (name) VALUES (p_group_name) RETURNING id INTO v_group_id;
        RAISE NOTICE 'Group "%" created.', p_group_name;
    END IF;

    UPDATE contacts SET group_id = v_group_id WHERE id = v_contact_id;

    RAISE NOTICE 'Contact "%" moved to group "%".', p_contact_name, p_group_name;
END;
$$;


-- ------------------------------------------------------------
-- 3.4 c)  search_contacts  (extends Practice 8 pattern-search)
--   Matches against: name, email, and ALL phones in phones table.
--   Returns one row per contact with aggregated phones.
-- ------------------------------------------------------------
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE (
    id         INTEGER,
    name       VARCHAR,
    email      VARCHAR,
    birthday   DATE,
    group_name VARCHAR,
    phones     TEXT,
    created_at TIMESTAMP
)
LANGUAGE plpgsql AS $$
DECLARE
    v_pattern TEXT := '%' || p_query || '%';
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.name,
        c.email,
        c.birthday,
        g.name        AS group_name,
        STRING_AGG(p.phone || ' (' || p.type || ')', ', ' ORDER BY p.id) AS phones,
        c.created_at
    FROM contacts c
    LEFT JOIN groups g ON g.id = c.group_id
    LEFT JOIN phones p ON p.contact_id = c.id
    WHERE
        c.name  ILIKE v_pattern
        OR c.email ILIKE v_pattern
        OR p.phone ILIKE v_pattern
    GROUP BY c.id, c.name, c.email, c.birthday, g.name, c.created_at
    ORDER BY c.name;
END;
$$;


-- ------------------------------------------------------------
-- Helper view: full contact card (convenient for SELECT *)
-- ------------------------------------------------------------
CREATE OR REPLACE VIEW v_contacts AS
SELECT
    c.id,
    c.name,
    c.email,
    c.birthday,
    g.name                                                     AS group_name,
    STRING_AGG(p.phone || ' (' || p.type || ')', ', ' ORDER BY p.id) AS phones,
    c.created_at
FROM contacts c
LEFT JOIN groups g ON g.id = c.group_id
LEFT JOIN phones p ON p.contact_id = c.id
GROUP BY c.id, c.name, c.email, c.birthday, g.name, c.created_at;
