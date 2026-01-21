const BASE_URL = "http://127.0.0.1:8000";

export async function fetchEmails() {
  const response = await fetch(`${BASE_URL}/emails`);
  return response.json();
}
