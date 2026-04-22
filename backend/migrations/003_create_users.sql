-- Migration: Create users table
-- Date: 2026-02-17
-- Feature: Auth — signup/signin

CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    name VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT now()
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_users_email ON users(email);

-- Rollback:
-- DROP TABLE IF EXISTS users;
