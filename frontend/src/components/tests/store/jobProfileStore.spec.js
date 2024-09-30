import { setActivePinia, createPinia } from "pinia";
import { useJobProfileStore } from "@/store/jobProfileStore";
import jobProfileService from "@/services/job_profile.service"; 

jest.mock("@/services/job_profile.service"); // Mock the service

describe("JobProfileStore", () => {
  beforeEach(() => {
    setActivePinia(createPinia()); // Set up Pinia before each test
  });

  it("should initialize with default values", () => {
    const store = useJobProfileStore();
    expect(store.profile).toBe("");
    expect(store.profileID).toBeUndefined();
  });

  it("should set the profile correctly", () => {
    const store = useJobProfileStore();
    const profile = "Innendienst";

    store.setProfile(profile);

    expect(store.profile).toEqual(profile);
  });

  it("should set the profileID correctly", () => {
    const store = useJobProfileStore();
    const profileID = 7;

    store.setProfileID(profileID);

    expect(store.profileID).toBe(profileID);
  });

  it("should fetch job profiles from the API", async () => {
    const store = useJobProfileStore();
    const mockProfiles = [
      {
        id: 1,
        job_name: "Innendienst",
        job_description: "Beispiel Beschriebung",
        job_tasks: "Beispielhafte Aufgaben",
      },
      {
        id: 1,
        job_name: "Außendienst",
        job_description: "Beispiel Beschriebung",
        job_tasks: "Beispielhafte Aufgaben",
      },
    ];

    jobProfileService.getJobProfiles.mockResolvedValue(mockProfiles);

    const response = await store.getJobProfiles();

    expect(response).toEqual(mockProfiles);
    expect(jobProfileService.getJobProfiles).toHaveBeenCalled();
  });

  it("should handle API errors in getJobProfiles", async () => {
    const store = useJobProfileStore();
    const consoleSpy = jest.spyOn(console, "log").mockImplementation(() => {});

    jobProfileService.getJobProfiles.mockRejectedValue(new Error("API Error"));

    const response = await store.getJobProfiles();

    expect(response).toBeUndefined();
    expect(consoleSpy).toHaveBeenCalledWith(new Error("API Error"));

    consoleSpy.mockRestore();
  });
});
