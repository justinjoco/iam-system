CREATE TABLE IF NOT EXISTS "audit_entity" (
    date_created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    date_updated TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    PRIMARY KEY (date_created, date_updated)
);

CREATE TABLE IF NOT EXISTS "user"(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    is_deactivated BOOLEAN NOT NULL DEFAULT FALSE
) INHERITS ("audit_entity");

CREATE TABLE IF NOT EXISTS "password"(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES "user"(id) NOT NULL,
    salted_password_hash TEXT NOT NULL,
    salt TEXT NOT NULL
) INHERITS ("audit_entity");

CREATE TABLE IF NOT EXISTS "role"(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL
) INHERITS ("audit_entity") ;

CREATE TABLE IF NOT EXISTS "permission"(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    action TEXT NOT NULL,
    resource TEXT NOT NULL
) INHERITS ("audit_entity") ;
CREATE INDEX permission_value_idx ON "permission"(action, resource);

CREATE TABLE IF NOT EXISTS "user_role"(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES "user"(id) NOT NULL,
    role_id UUID REFERENCES "role"(id) NOT NULL
) INHERITS ("audit_entity");

CREATE TABLE IF NOT EXISTS "role_permission"(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    role_id UUID REFERENCES "role"(id) NOT NULL,
    permission_id UUID REFERENCES "permission"(id) NOT NULL
) INHERITS ("audit_entity");

CREATE TABLE IF NOT EXISTS "permission_context"(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    permission_id UUID REFERENCES "permission"(id) NOT NULL,
    resource_id UUID NOT NULL
) INHERITS ("audit_entity");

CREATE TABLE IF NOT EXISTS "refresh_token"(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES "user"(id) NOT NULL,
    expiry_date TIMESTAMP WITH TIME ZONE NOT NULL,
    scopes TEXT[] NOT NULL DEFAULT array[]::text[],
    is_expired BOOLEAN NOT NULL DEFAULT FALSE,
    parent_id UUID REFERENCES "refresh_token"(id)
) INHERITS ("audit_entity");

CREATE TABLE IF NOT EXISTS "authorization_code"(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES "user"(id) NOT NULL,
    expiry_date TIMESTAMP WITH TIME ZONE NOT NULL,
    code_challenge TEXT NOT NULL,
    code_challenge_method TEXT NOT NULL
) INHERITS ("audit_entity");

CREATE TABLE IF NOT EXISTS "login_audit"(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES "user"(id) NOT NULL
) INHERITS ("audit_entity");

CREATE TABLE IF NOT EXISTS "client_credentials"(
    id UUID PRIMARY KEY,
    salted_secret_hash TEXT NOT NULL,
    salt TEXT NOT NULL
) INHERITS ("audit_entity");