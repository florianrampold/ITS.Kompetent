import { setActivePinia, createPinia } from "pinia";
import { useTrainingsStore } from "@/store/TrainingsStore"; // Adjust the path as necessary
import trainingsService from "@/services/trainings.service"; 
jest.mock("@/services/trainings.service"); // Mock the service

describe("TrainingsStore", () => {
  beforeEach(() => {
    setActivePinia(createPinia()); // Set up Pinia before each test
    jest.resetAllMocks(); // Reset mocks before each test
  });

  it("should fetch training programs from the API", async () => {
    const store = useTrainingsStore();
    const mockTrainings = [
      {
        id: 1,
        training_group: "TG1",
        training_provider: "ExampleProvider",
        delivery_method: {
          id: 3,
          delivery_method: "MOOC",
          costs_name: "Kostenlos",
          certification: "Nein",
          language: { id: 1, language: "Deutsch" },
          training_url: "https://example-training.com",
          competence_dimensions: {
            dimension_description:
              "Lokalisierung von Gefahrenquellen in typischen Handlungssituationen des eigenen Stellenprofils",
            dimension_name: "Threat Awareness",
            id: 1,
          },
          threat_event: {
            id: 2,
            event_name: "Phishing",
            event_description:
              "Der Angreifer fälscht Mitteilungen einer legitimen Quelle, um an vertrauliche Informationen zu gelangen",
          },
          competence_dimension_count: 2,
          matchingScore: 53,
          matchingScorePerCompetenceDimension: [17.5, 5, 8, 2, 0, 0, 0],
          pageNumber: 1,
          rank: 1,
        },
      },
      { id: 2, name: "Training 2" },
    ];

    trainingsService.getTrainings.mockResolvedValue(mockTrainings);

    const response = await store.getTrainings();

    expect(response).toEqual(mockTrainings);
    expect(trainingsService.getTrainings).toHaveBeenCalled();
  });

  it("should fetch training categories from the API", async () => {
    const store = useTrainingsStore();
    const mockCategories = [
      {
        id: 1,
        training_catgeory_name: "Social Engineering",
        training_category_description: "Beispiel Beschreibung",
        threat_events: [
          {
            id: 2,
            event_name: "Phishing",
            event_description:
              "Der Angreifer fälscht Mitteilungen einer legitimen Quelle, um an vertrauliche Informationen zu gelangen",
          },
        ],
      },
    ];

    trainingsService.getTrainingCategories.mockResolvedValue(mockCategories);

    const response = await store.getTrainingCategories();

    expect(response).toEqual(mockCategories);
    expect(trainingsService.getTrainingCategories).toHaveBeenCalled();
  });

  it("should fetch job profiles by training categories from the API", async () => {
    const store = useTrainingsStore();
    const mockJobProfilesWIthTrainingCategories = [
      {
        job_profile_id: 1,
        job_name: "Innendienst",
        job_description: "Beispiel Beschreibung",
        threat_events: [
          {
            id: 2,
            event_name: "Phishing",
            event_description:
              "Der Angreifer fälscht Mitteilungen einer legitimen Quelle, um an vertrauliche Informationen zu gelangen",
          },
        ],
      },
    ];

    trainingsService.getJobProfilesByTrainingCategories.mockResolvedValue(
      mockJobProfilesWIthTrainingCategories
    );

    const response = await store.getJobProfilesByTrainingCategories();

    expect(response).toEqual(mockJobProfilesWIthTrainingCategories);
    expect(
      trainingsService.getJobProfilesByTrainingCategories
    ).toHaveBeenCalled();
  });
});
