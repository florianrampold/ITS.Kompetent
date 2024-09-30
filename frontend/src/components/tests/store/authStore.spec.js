import { setActivePinia, createPinia } from "pinia";
import { useAuthStore } from "@/store/AuthStore";
import authService from "@/services/auth.service";
import router from "@/router";

jest.mock("@/services/auth.service");
jest.mock("@/router", () => ({
  push: jest.fn(),
  currentRoute: { value: { matched: [] } },
}));

describe("AuthStore", () => {
  beforeEach(() => {
    setActivePinia(createPinia()); // Set up Pinia
  });

  it("should set the last interaction timestamp", () => {
    const store = useAuthStore();
    const timestamp = "2024-08-26T12:34:56Z";

    store.setLastInteraction(timestamp);

    expect(store.lastInteraction).toBe(timestamp);
  });

  it("should initialize and set the user when authenticated", async () => {
    const store = useAuthStore();
    const mockUser = { username: "testuser" };

    authService.getStatus.mockResolvedValueOnce({
      status: "authenticated",
      user: mockUser,
    });

    await store.init(false);

    expect(store.isLoggedIn).toBe(true);
    expect(store.user).toEqual(mockUser);
    expect(store.isInitializing).toBe(false);
  });

  it("should log the user out if not authenticated", async () => {
    const store = useAuthStore();

    authService.getStatus.mockResolvedValueOnce({
      status: "unauthenticated",
    });

    // Mock currentRoute to include a route that requires authentication
    router.currentRoute.value.matched = [{ meta: { requiresAuth: true } }];

    await store.init(false);

    expect(store.isLoggedIn).toBe(false);
    expect(store.user).toBeNull();
    expect(router.push).toHaveBeenCalledWith("/login");
  });

  it("should log the user in with valid credentials", async () => {
    const store = useAuthStore();
    const mockUser = { username: "testuser" };

    authService.login.mockResolvedValueOnce({ user: mockUser });

    await store.login({ username: "test", password: "password" });

    expect(store.isLoggedIn).toBe(true);
    expect(store.user).toEqual(mockUser);
  });

  it("should handle login errors", async () => {
    const store = useAuthStore();
    const mockError = new Error("Invalid credentials");

    authService.login.mockRejectedValueOnce(mockError);

    await expect(
      store.login({ username: "test", password: "wrongpassword" })
    ).rejects.toThrow(mockError);

    expect(store.isLoggedIn).toBe(false);
  });

  it("should log the user out and stop the token expiry timer", async () => {
    const store = useAuthStore();

    // Mock the clearInterval function
    jest.spyOn(global, "clearInterval");

    authService.logout.mockResolvedValueOnce({});

    // Start the token expiry timer
    store.startTokenExpiryTimer();

    // Save the interval ID for comparison
    const intervalId = store.refreshInterval;

    // Call the logout method
    await store.logout(false);

    expect(store.isLoggedIn).toBe(false);
    expect(store.user).toBeNull();
    expect(clearInterval).toHaveBeenCalledWith(intervalId);
    expect(router.push).toHaveBeenCalledWith("/login");

    // Restore the original clearInterval function
    clearInterval.mockRestore();
  });

  it("should refresh the token", async () => {
    const store = useAuthStore();

    authService.refreshToken.mockResolvedValueOnce({});

    await store.refreshToken();

    expect(authService.refreshToken).toHaveBeenCalledWith(
      store.lastInteraction
    );
  });

  it("should log the user out if token refresh fails with session expired", async () => {
    const store = useAuthStore();
    const mockError = {
      response: {
        data: {
          error: "Session expired. Please log in again.",
        },
      },
    };

    authService.refreshToken.mockRejectedValueOnce(mockError);

    await store.refreshToken();

    expect(store.isLoggedIn).toBe(false);
    expect(router.push).toHaveBeenCalledWith("/login");
  });
});
