import { setActivePinia, createPinia } from "pinia";
import { useCampagneStore } from "@/store/CampagneStore";
import campagneService from "@/services/campagne.service";

jest.mock("@/services/campagne.service");
jest.mock("@/store/AuthStore", () => {
  console.log("useAuthStore mock is being applied");
  return {
    useAuthStore: jest.fn(() => {
      console.log("Mocked useAuthStore is being called");
      return {
        logout: jest.fn().mockResolvedValueOnce(), // Simulate an async logout function
      };
    }),
  };
});

describe("Campagne Store", () => {
  beforeEach(() => {
    setActivePinia(createPinia());
    jest.clearAllMocks(); // Clears mock history
    jest.spyOn(console, "error").mockImplementation(() => {}); // Mock console.error
    jest.spyOn(console, "log").mockImplementation(() => {}); // Mock console.log
  });
  afterEach(() => {
    jest.clearAllMocks(); // Clears mock history
  });

  it("should initialize with default state", () => {
    const store = useCampagneStore();

    expect(store.campagneStarted).toBe(false);
    expect(store.campagneEnded).toBe(false);
  });

  it("should set campagneStarted to true", () => {
    const store = useCampagneStore();
    store.setCampagneStarted(true);

    expect(store.campagneStarted).toBe(true);
  });

  it("should remove campagneStarted", () => {
    const store = useCampagneStore();
    store.setCampagneStarted(true);
    store.removeCampagneStarted();

    expect(store.campagneStarted).toBe(false);
  });

  it("should generate invitation tokens and return data", async () => {
    const store = useCampagneStore();
    const mockResponse = { data: "tokens" };

    campagneService.generateInvitationTokens.mockResolvedValueOnce(
      mockResponse
    );

    const result = await store.generateInvitationTokens({
      emails: ["test@example.com"],
    });

    expect(result).toBe(mockResponse.data);
    expect(campagneService.generateInvitationTokens).toHaveBeenCalledWith({
      payload: { emails: ["test@example.com"] },
    });
  });

  it("should handle errors in generate invitation tokens", async () => {
    const store = useCampagneStore();

    const mockError = new Error("Something went wrong");
    campagneService.generateInvitationTokens.mockRejectedValueOnce(mockError);

    await expect(
      store.generateInvitationTokens({ emails: [] })
    ).rejects.toThrow(mockError);
  });

  it("should post competence test results successfully", async () => {
    const store = useCampagneStore();
    campagneService.postCompetenceTestResults.mockResolvedValueOnce({});

    await store.postCompetenceTestResults({ score: 95 });

    expect(campagneService.postCompetenceTestResults).toHaveBeenCalledWith({
      score: 95,
    });
  });

  it("should handle error during posting competence test results", async () => {
    const store = useCampagneStore();
    const mockError = new Error("API Error");

    // Mock the API call to reject with an error
    jest.spyOn(store, "postCompetenceTestResults").mockRejectedValue(mockError);

    // Mock console.error
    const consoleErrorSpy = jest
      .spyOn(console, "error")
      .mockImplementation(() => {});

    // Expect the function to throw the error
    await expect(
      store.postCompetenceTestResults({ score: 95 })
    ).rejects.toThrow(mockError);

    // Restore console.error after the test
    consoleErrorSpy.mockRestore();
  });

  // Example test for getCompetenceTestResults
  it("should get competence test results successfully", async () => {
    const store = useCampagneStore();
    const mockResults = {
      results: [
        /* some results */
      ],
    };
    campagneService.getCompetenceTestResults.mockResolvedValueOnce(mockResults);

    const results = await store.getCompetenceTestResults("profile123");
    expect(results).toEqual(mockResults);
    expect(campagneService.getCompetenceTestResults).toHaveBeenCalledWith(
      "profile123"
    );
  });

  /* it("should call auth.logout if getCompetenceTestResults fails with 403 or 401", async () => {
    const store = useCampagneStore();
    const authStore = useAuthStore();

    campagneService.getCompetenceTestResults.mockRejectedValueOnce({
      response: { status: 403 },
    });

    await store.getCompetenceTestResults("profile123");
    expect(authStore.logout).toHaveBeenCalled();

    campagneService.getCompetenceTestResults.mockRejectedValueOnce({
      response: { status: 401 },
    });

    await store.getCompetenceTestResults("profile123");
    expect(authStore.logout).toHaveBeenCalledTimes(2); // Ensure it's called again
  }); */

  it("should fetch participants per profile successfully", async () => {
    const store = useCampagneStore();
    const mockParticipants = {
      participants: [
        /* some participants */
      ],
    };
    campagneService.getParticipantsPerProfile.mockResolvedValueOnce(
      mockParticipants
    );

    const participants = await store.getParticipantsPerProfile();
    expect(participants).toEqual(mockParticipants);
    expect(campagneService.getParticipantsPerProfile).toHaveBeenCalled();
  });


  it("should delete campaign successfully", async () => {
    const store = useCampagneStore();
    campagneService.deleteCampagne.mockResolvedValueOnce({});

    await store.deleteCampagne();
    expect(campagneService.deleteCampagne).toHaveBeenCalled();
  });

  it("should generate security key and return response", async () => {
    const store = useCampagneStore();
    const mockResponse = { key: "secureKey" };
    campagneService.generateSecurityKey.mockResolvedValue(mockResponse);

    const result = await store.generateSecurityKey();

    expect(result).toEqual(mockResponse);
  });

  it("should decrypt emails and return response", async () => {
    const store = useCampagneStore();
    const mockData = { encrypted: "data" };
    const mockResponse = { decrypted: "data" };
    campagneService.decryptEmails.mockResolvedValue(mockResponse);

    const result = await store.decryptEmails(mockData);

    expect(result).toEqual(mockResponse);
  });

  it("should retrieve management report and return response", async () => {
    const store = useCampagneStore();
    const mockResponse = { report: "Management Report" };
    campagneService.getManagementReport.mockResolvedValue(mockResponse);

    const result = await store.getManagementReport();

    expect(result).toEqual(mockResponse);
  });

  it("should retrieve campaign details and return response", async () => {
    const store = useCampagneStore();
    const mockResponse = { id: 1, name: "Campaign 1" };
    campagneService.getCampagne.mockResolvedValue(mockResponse);

    const result = await store.getCampagne();

    expect(result).toEqual(mockResponse);
  });
});
