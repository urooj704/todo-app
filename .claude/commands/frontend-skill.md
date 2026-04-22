---
description: Build frontend pages, components, layouts, and styling for modern web applications.
handoffs:
  - label: Build Frontend Pages
    agent: frontend-nextjs
    prompt: Implement the frontend pages and components with proper styling and data fetching.
  - label: Create Backend API
    agent: fastapi-backend
    prompt: Create the backend API endpoints that the frontend will consume.
---

# Frontend Skill

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Instructions

### 1. Page & Layout Structure

- Build pages using a clear routing structure
- Define reusable layouts and templates
- Maintain consistent spacing and hierarchy
- Support responsive and mobile-first design

### 2. Component Design

- Create reusable and composable components
- Keep components focused and single-purpose
- Manage component state predictably
- Separate presentational and logic components

### 3. Styling

- Apply consistent styling patterns
- Use modern CSS approaches (CSS Modules, Tailwind, styled components)
- Ensure responsive behavior across screen sizes
- Maintain theme consistency (colors, typography)

### 4. Data & Interaction

- Connect components to backend APIs
- Handle loading, empty, and error states
- Reflect authentication-aware UI states
- Manage client-side interactions cleanly

### 5. Accessibility & UX

- Use semantic HTML elements
- Ensure keyboard and screen-reader support
- Provide clear visual feedback
- Optimize for usability and clarity

## Best Practices

- Prefer composition over duplication
- Keep UI logic simple and predictable
- Build mobile-first, then enhance
- Avoid over-styling components
- Optimize rendering and re-renders
- Follow framework conventions

## Example Structure (JSX)

```tsx
<Layout>
  <PageHeader title="Dashboard" />
  <MainContent>
    <Card>
      <h2>My Tasks</h2>
      <TaskList />
    </Card>
  </MainContent>
</Layout>
```

## Execution Steps

1. **Analyze Requirements**: Review $ARGUMENTS to understand the UI needs.

2. **Check Existing Components**: Search for existing components and patterns.

3. **Design Component Hierarchy**: Based on requirements, design:
   - Page structure
   - Layout components
   - Reusable UI components
   - State management approach

4. **Create Layout Structure**:
   - Define page layouts
   - Set up routing
   - Implement navigation
   - Add responsive breakpoints

5. **Build Components**:
   - Create presentational components
   - Add interactivity and state
   - Connect to data sources
   - Handle loading/error states

6. **Apply Styling**:
   - Implement design system
   - Add responsive styles
   - Ensure theme consistency
   - Polish animations/transitions

7. **Ensure Accessibility**:
   - Add ARIA labels
   - Test keyboard navigation
   - Verify screen reader support
   - Check color contrast

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent-native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3-7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` -> `history/prompts/constitution/`
     - Feature stages -> `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` -> `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent-native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/...`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.
