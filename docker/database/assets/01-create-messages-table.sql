CREATE TABLE IF NOT EXISTS public.messages (
    id UUID PRIMARY KEY,
    destination TEXT NOT NULL,
    type TEXT NOT NULL,
    body JSONB NOT NULL DEFAULT '{}'::JSONB,
    deliver_after TIMESTAMP NOT NULL CHECK (deliver_after > NOW()),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
