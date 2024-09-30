import { setActivePinia, createPinia } from "pinia";
import { useCompetenceTestStore } from "@/store/competenceTestStore";
import competenceTestService from "@/services/competence_test.service";

jest.mock("@/services/competence_test.service");

describe("CompetenceTest Store", () => {
  beforeEach(() => {
    setActivePinia(createPinia());
    jest.clearAllMocks(); // Clear mock calls between tests
    jest.spyOn(console, "error").mockImplementation(() => {}); // Mock console.error
    jest.spyOn(console, "log").mockImplementation(() => {}); // Mock console.log
  });
  afterEach(() => {
    jest.restoreAllMocks();
  });

  it("should set competence test result correctly", () => {
    const store = useCompetenceTestStore();
    const mockResult = {
      test_situations: { id: 49 },
      job_profile_id: 7,
      competence_dimension_score: { label: "Threat Awareness", score: 1 },
    };

    store.setCompetenceTestResult(mockResult);

    expect(store.competenceTestResult).toEqual(mockResult);
  });

  it("should get competence test result correctly", () => {
    const store = useCompetenceTestStore();
    const mockResult = {
      test_situations: { id: 49 },
      job_profile_id: 7,
      competence_dimension_score: { label: "Threat Awareness", score: 1 },
    };

    store.setCompetenceTestResult(mockResult);

    expect(store.getCompetenceTestResult).toEqual(mockResult);
  });

  it("should fetch competence test details successfully", async () => {
    const store = useCompetenceTestStore();
    const mockDetails = {
      testSituations: {
        id: 49,
        threat_situation_identifier: "4.5",
        threat_description:
          "Sie nutzen einen Messenger dienstlich auf Ihrem Handy...",
        threat_vector: {
          id: 40,
          threat_area: {
            area_description:
              "Eine Softwareanwendung, die Echzeitkommunukation über das Internet eröglicht.",
          },
          are_name: "Instantmessenger",
          id: 4,
        },
        threat_event: {
          event_description:
            "Der Angreifer nutzt gängige Übermittlungsmechanismen...",
          event_name: "Einschleusen bekannter Malware...",
          id: 3,
        },
        threat_vector_description: "Der Angreifer nutzt...",
        job_profile: {
          id: 7,
          job_description: "",
          job_name: "",
          job_tasks: "",
        },
      },
    };
    competenceTestService.getCompetenceTest.mockResolvedValueOnce(mockDetails);

    const result = await store.getCompetenceTest(7);

    expect(result).toEqual(mockDetails);
    expect(competenceTestService.getCompetenceTest).toHaveBeenCalledWith(7);
  });

  it("should fetch test items successfully", async () => {
    const store = useCompetenceTestStore();
    const mockItems = [
      {
        competence_dimension: {
          dimension_description:
            "Lokalisierung von Gefahrenquellen in typischen Handlungssituationen des eigenen Stellenprofils",
          dimension_name: "Threat Awareness",
          id: 1,
        },
      },
    ];
    competenceTestService.getTestItems.mockResolvedValueOnce(mockItems);

    const result = await store.getTestItems(4);

    expect(result).toEqual(mockItems);
    expect(competenceTestService.getTestItems).toHaveBeenCalledWith(4);
  });

  it("should fetch impulse items successfully", async () => {
    const store = useCompetenceTestStore();
    const activeImpulsItems = {
      id: 47,
      image: [
        {
          id: 120,
          image_description: "",
          image_field:
            "http://localhost:8000/media/static/images/AP_4.5_Impuls1.png",
          impulse_number: "Impuls 1",
          threat_situation: 49,
        },
      ],
      impulse_text:
        "Hierzu werden Ihnen im Folgenden drei unterschiedliche Szenarien skizziert.",
      resourcetype: "ImageImpulse",
    };
    competenceTestService.getImpulseItems.mockResolvedValueOnce(
      activeImpulsItems
    );

    const result = await store.getImpulseItems(5);

    expect(result).toEqual(activeImpulsItems);
    expect(competenceTestService.getImpulseItems).toHaveBeenCalledWith(5);
  });

  it("should fetch answer options successfully", async () => {
    const store = useCompetenceTestStore();
    const mockOptions = [
      { answer_rating: 1, id: 1897, option: "Szenario 1." },
      { answer_rating: 2, id: 1898, option: "Szenario 2." },
      { answer_rating: 0, id: 1899, option: "Szenario 3." },
    ];
    competenceTestService.getAnswerOptions.mockResolvedValueOnce(mockOptions);

    const result = await store.getAnswerOptions(4);

    expect(result).toEqual(mockOptions);
    expect(competenceTestService.getAnswerOptions).toHaveBeenCalledWith(4);
  });

  it("should generate individual report successfully", async () => {
    const store = useCompetenceTestStore();
    const mockReport = { report: "Generated report" };
    competenceTestService.generateIndividualReport.mockResolvedValueOnce(
      mockReport
    );

    const result = await store.generateIndividualReport({
      results: "test results",
    });

    expect(result).toEqual(mockReport);
    expect(competenceTestService.generateIndividualReport).toHaveBeenCalledWith(
      { results: "test results" }
    );
  });

  it("should handle error during report generation", async () => {
    const store = useCompetenceTestStore();
    const mockError = new Error("Report generation failed");
    competenceTestService.generateIndividualReport.mockRejectedValueOnce(
      mockError
    );

    await expect(
      store.generateIndividualReport({ results: "test results" })
    ).rejects.toThrow(mockError);
    expect(console.error).toHaveBeenCalledWith(
      "Error during report generation:",
      mockError
    );
  });

  it("should fetch competence dimensions successfully", async () => {
    const store = useCompetenceTestStore();
    const mockDimensions = [
      { dimension_name: "Threat Awareness", dimension_description: "" },
    ];
    competenceTestService.getCompetenceDimensions.mockResolvedValueOnce(
      mockDimensions
    );

    const result = await store.getCompetenceDimensions();

    expect(result).toEqual(mockDimensions);
    expect(competenceTestService.getCompetenceDimensions).toHaveBeenCalled();
  });

  it("should handle error fetching competence dimensions", async () => {
    const store = useCompetenceTestStore();
    const mockError = new Error("Fetching dimensions failed");
    competenceTestService.getCompetenceDimensions.mockRejectedValueOnce(
      mockError
    );

    await expect(store.getCompetenceDimensions()).rejects.toThrow(mockError);
    expect(console.error).toHaveBeenCalledWith(
      "Error fetching competence dimensions:",
      mockError
    );
  });

  it("should send contact request successfully", async () => {
    const store = useCompetenceTestStore();
    const mockResponse = { success: true };
    competenceTestService.sendContactRequest.mockResolvedValueOnce(
      mockResponse
    );

    const result = await store.sendContactRequest({
      name: "John Doe",
      message: "Hello, I would like to test ITS.kompetent!",
      email: "john.doe@example.com",
    });

    expect(result).toEqual(mockResponse);
    expect(competenceTestService.sendContactRequest).toHaveBeenCalledWith({
      name: "John Doe",
      message: "Hello, I would like to test ITS.kompetent!",
      email: "john.doe@example.com",
    });
  });

  it("should handle error during sending contact request", async () => {
    const store = useCompetenceTestStore();
    const mockError = new Error("Contact request failed");
    competenceTestService.sendContactRequest.mockRejectedValueOnce(mockError);

    await store.sendContactRequest({
      name: "John Doe",
      message: "Hello, I would like to test ITS.kompetent!",
      email: "john.doe@example.com",
    });

    expect(console.log).toHaveBeenCalledWith(mockError);
  });
});
