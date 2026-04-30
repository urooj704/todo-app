/**
 * Authentication client for FastAPI auth endpoints.
 * Handles signin, signup, signout, and session management.
 */

import { api } from './api';
import { User, Session } from './types';

// Base URL for auth — same FastAPI server as the rest of the API
function normalizeApiBaseUrl(raw: string | undefined): string {
  const fallback = 'http://localhost:8000/api';
  const base = (raw || fallback).replace(/\/+$/, '');
  return base.endsWith('/api') ? base : `${base}/api`;
}

const AUTH_BASE = normalizeApiBaseUrl(process.env.NEXT_PUBLIC_API_URL);

// Simple in-memory session storage (in production, use secure cookies)
let currentSession: Session | null = null;

/**
 * Get the current session.
 */
export function getSession(): Session | null {
  return currentSession;
}

/**
 * Check if user is authenticated.
 */
export function isAuthenticated(): boolean {
  return currentSession !== null;
}

/**
 * Sign up a new user.
 */
export async function signUp(
  email: string,
  password: string,
  name?: string
): Promise<Session> {
  const response = await fetch(`${AUTH_BASE}/auth/signup`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password, name }),
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Signup failed' }));
    throw new Error(error.detail || 'Signup failed');
  }

  const data = await response.json();
  currentSession = {
    user: data.user,
    accessToken: data.accessToken,
  };

  api.setToken(currentSession.accessToken);
  return currentSession;
}

/**
 * Sign in an existing user.
 */
export async function signIn(
  email: string,
  password: string
): Promise<Session> {
  const response = await fetch(`${AUTH_BASE}/auth/signin`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password }),
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Invalid credentials' }));
    throw new Error(error.detail || 'Invalid credentials');
  }

  const data = await response.json();
  currentSession = {
    user: data.user,
    accessToken: data.accessToken,
  };

  api.setToken(currentSession.accessToken);
  return currentSession;
}

/**
 * Sign out the current user.
 */
export async function signOut(): Promise<void> {
  try {
    await fetch(`${AUTH_BASE}/auth/signout`, { method: 'POST' });
  } catch {
    // Ignore errors during signout
  }

  currentSession = null;
  api.setToken(null);
}

/**
 * Restore session from storage (call on app init).
 */
export async function restoreSession(): Promise<Session | null> {
  // No persistent token storage — session is in-memory only.
  // To persist across page refreshes, store the token in localStorage here.
  return null;
}
