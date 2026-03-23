const { test, expect } = require('@playwright/test');

test('calculator UI test', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/docs');

  // Check API docs loaded
  await expect(page).toHaveTitle(/FastAPI/);
});