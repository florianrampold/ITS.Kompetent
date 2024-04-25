<template>
  <Hero
    ><template #title>
      <div
        class="flex justify-center items-center lg:items-start lg:justify-start"
      >
        <h1 class="main-heading">
          <span class="text-primary font-semibold">Antworten auf <br /> </span>
          {{ " " }}
          <span class="text-secondary xl:inline">Ihre Fragen</span>
        </h1>
      </div>
    </template>
    <template #content>
      <div
        class="flex justify-center items-center lg:items-start lg:justify-start"
      >
        <p
          class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl md:mt-5 md:text-xl lg:mx-0"
        >
          Herzlich willkommen im KMU-Kampagnen-Management! Ihnen wurde von Ihrem
          bzw. Ihrer Administrator*in die Rolle des/der KMU-Kampagnen-Manager*in
          zugewiesen. In dieser Ansicht erhalten Sie Informationen zu
          ITS.kompetent. Wir beantworten Ihnen die drei Fragen:
          <br />
          <br />
          <strong>Was ist ITS.kompetent?</strong> <br />
          <strong>Wie funktioniert ITS.kompetent?</strong> <br />
          <strong
            >Welche Funktionen bietet das KMU-Kampagnen-Management?</strong
          >
        </p>
      </div>
    </template>

    <template #image>
      <transition appear name="fade">
        <div class="grow-0 shrink-1 md:shrink-0 basis-auto mb-12 md:mb-0">
          <img
            src="@/assets/questions.jpg"
            class="w-full"
            alt="Sample image"
          /></div></transition
    ></template>
    <template #progress>
      <!-- Tabs Navigation -->
      <div
        ref="scrollTarget"
        class="flex space-x-1 justify between bg-gray-200 p-2 rounded-lg"
      >
        <button
          v-for="tab in tabs"
          :key="tab.id"
          :class="[
            'flex-1 text-center px-4 py-2 rounded-lg',
            tab.id === activeTabId ? 'bg-white shadow' : 'text-gray-600',
          ]"
          @click="changeTab(tab.id)"
        >
          {{ tab.text }}
        </button>
      </div>
    </template>
  </Hero>
  <div v-if="activeTabId === 'tab1'">
    <main class="bg-white pt-40 pb-20">
      <h1 class="main-heading pb-20">Unser Ansatz</h1>
      <div class="flex flex-row justify-center items-center">
        <div class="border-b-4 rounded-lg w-14 border-secondary mb-40"></div>
      </div>

      <div class="standard-container">
        <div
          class="flex flex-col sm:flex-row justify-center lg:justify-start flex-wrap"
        >
          <div
            class="w-full lg:w-1/2 text-center lg:text-left divide-secondary"
          >
            <h1 class="main-heading">
              <span class="text-primary xl:inline">Beschreibung<br /> </span>
            </h1>
            <p
              class="pt-8 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
            >
              Das Projekt ITS.Kompetent unterstützt KMUs dabei, die Kompetenzen
              der Mitarbeiter:innen im Bereich der Informationstechnischen
              Sicherheit (ITS-Kompetenzen) realitätsnah zu messen und mit den
              berufsbezogenen Anforderungen abzugleichen. Mit Hilfe von
              ITS.Kompetent können KMUs ihren unternehmensspezifischen
              Qualifizierungsbedarf ermitteln und geeignete Schulungsangebote
              ausarbeiten. Dazu wurde ein online-gestütztes ITS-Analysetool mit
              Hilfe von wissenschaftlichen Methoden entwickelt und hiermit KMUs
              zur Verfügung gestellt. Das Tool integriert Anforderungen,
              Methoden zur Kompetenzmessung und Vorschläge für
              Weiterbildungsmaßnahmen.
            </p>
          </div>
          <transition appear name="fade">
            <div
              class="grow-0 shrink-1 md:shrink-0 basis-auto xl:w-6/12 lg:w-6/12 md:w-6/12 mt-10 mb-12 md:mb-0"
            >
              <img
                :src="require('@/assets/lifecycle.svg')"
                class="w-full"
                alt="Matching of ITS-competencies"
              /></div
          ></transition>
        </div>

        <div class="flex sm:flex-row justify-center flex-wrap"></div>
      </div>
    </main>
    <div class="page-background pb-40">
      <div class="grid grid-cols-1">
        <h1 class="main-heading pb-20 pt-40">Unsere Services</h1>
        <div class="flex flex-row justify-center items-center">
          <div class="border-b-4 rounded-lg w-14 border-secondary mb-40"></div>
        </div>
        <h1
          class="text-xl tracking-tight font-extrabold text-secondary flex items-center justify-center sm:text-3xl md:text-4xl py-20"
        >
          Für KMUs
        </h1>
      </div>
      <div class="standard-container">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-10 lg:gap-20 xl:gap-40">
          <!-- <IconCard
          ><template #title>Registrieren Sie Ihr KMU</template>
          <template #icon>
            <LoginIcon
              class="h-32 w-32 text-secondary hover:text-secondaryAccent"
            >
            </LoginIcon>
          </template>
          ></IconCard
        > -->
          <IconCard
            ><template #title
              >Analyse der ITS-Kompetenzen Ihrer Mitarbeiter:innen
            </template>
            <template #icon>
              <MagnifyingGlassIcon
                class="h-32 w-32 text-secondary hover:text-secondaryAccent"
              >
              </MagnifyingGlassIcon>
            </template>
          </IconCard>
          <IconCard
            ><template #title
              >Abruf von ITS-Kompetenzen der Mitarbeiter:innen auf freiwilliger
              Basis
            </template>
            <template #icon>
              <ChartBarIcon
                class="h-32 w-32 text-secondary hover:text-secondaryAccent"
              >
              </ChartBarIcon>
            </template>
          </IconCard>
        </div>
        <h1
          class="text-xl tracking-tight font-extrabold text-secondary flex items-center justify-center sm:text-3xl md:text-4xl py-20"
        >
          Für KMU-Mitarbeiter:innen
        </h1>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-10 lg:gap-20 xl:gap-40">
          <IconCard
            ><template #title
              >Erhalten Sie umfassende Statistiken zu ihren
              ITS-Fertigkeiten</template
            >
            <template #icon>
              <DocumentChartBarIcon
                class="h-32 w-32 text-secondary hover:text-secondaryAccent"
              >
              </DocumentChartBarIcon>
            </template>
          </IconCard>
          <IconCard
            ><template #title>Ermitteln Sie Ihre ITS-Kompetenzen </template>
            <template #icon>
              <ShieldCheckIcon
                class="h-32 w-32 text-secondary hover:text-secondaryAccent"
              >
              </ShieldCheckIcon>
            </template>
          </IconCard>
          <!-- <IconCard>
          <template #title>
            Erhalten Sie individuelle ITS-Trainingsangebote
          </template>
          <template #icon>
            <ViewGridIcon
              class="h-32 w-32 text-secondary hover:text-secondaryAccent"
            >
            </ViewGridIcon>
          </template>
        </IconCard> -->
        </div>
      </div>
    </div>

    <main class="bg-white pt-40 pb-20">
      <div class="standard-container">
        <h1 class="main-heading pb-20">Nutzen für KMUs</h1>
        <div class="flex flex-row justify-center items-center">
          <div class="border-b-4 rounded-lg w-14 border-secondary mb-40"></div>
        </div>
        <div
          class="flex flex-col sm:flex-row justify-center lg:justify-start flex-wrap"
        >
          <div
            class="w-full lg:w-1/2 text-center lg:text-left divide-secondary"
          >
            <h1 class="main-heading">
              <span class="text-primary xl:inline"
                >Matching von Anforderungsprofilen mit ITS-Kompetenzen<br />
              </span>
            </h1>
            <p
              class="pt-8 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
            >
              ITS.Kompetent ermöglicht die Identifizierung des KMU-spezifischen
              ITS-Qualifizierungsbedarfs durch einen Stellenprofilvergleich und
              die anschließende Auswahl passgenauer ITS-Ausbildungsangebote. Mit
              Hilfe von ITS.Kompetent gewinnen KMU Transparenz hinsichtlich der
              drei Fragen: Welche ITS-Kompetenzen werden bei welchen
              Mitarbeitern benötigt (Was?), wo liegt der berufsspezifische und
              unternehmensweite ITS-Qualifizierungsbedarf (Wo?) und wie können
              die fehlenden Kompetenzen effektiv aufgebaut werden (Wie?).
            </p>
          </div>
          <transition appear name="fade">
            <div
              class="grow-0 shrink-1 md:shrink-0 basis-auto xl:w-6/12 lg:w-6/12 md:w-6/12 mb-12 md:mb-0"
            >
              <img
                :src="require('@/assets/matching.jpg')"
                class="w-full"
                alt="Matching of ITS-competencies"
              /></div
          ></transition>
        </div>
        <div
          class="flex flex-col sm:flex-row justify-center lg:justify-end flex-wrap pt-40"
        >
          <transition appear name="fade">
            <div
              class="grow-0 shrink-1 md:shrink-0 basis-auto xl:w-6/12 lg:w-6/12 md:w-6/12 mb-12 md:mb-0"
            >
              <img
                src="@/assets/analytics.jpg"
                class="w-full"
                alt="ITS.kompetent analytics"
              /></div
          ></transition>
          <div
            class="w-full lg:w-1/2 text-center lg:text-left divide-secondary"
          >
            <h1 class="main-heading">
              <span class="text-primary xl:inline"
                >Detaillierte Statistiken über Mitarbeiter:innen-Kompetenzen
                <br />
              </span>
            </h1>
            <p
              class="pt-8 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
            >
              ITS.Kompetent stellt Ihren Mitarbeiter:innen ein
              benutzerfreundliches Dashboard zur Verfügung, das Informationen
              über den IST-Zustand der ITS-Kompetenzen für Mitarbeiter:innen aus
              verschiedenen Stellenprofilen enthält.
            </p>
          </div>
        </div>
        <div class="flex sm:flex-row justify-center flex-wrap"></div>
      </div>
    </main>
  </div>
  <div v-if="activeTabId === 'tab2'">
    <div class="page-background">
      <div class="standard-container flex flex-col justify-center">
        <h1 class="main-heading pb-20">
          <span class="text-primary xl:inline">In 4 Schritten</span>
          {{ " " }}
          <span class="text-secondary xl:inline">zum Ergebnis</span>
        </h1>
        <div class="flex flex-row justify-center items-center">
          <div class="border-b-4 rounded-lg w-14 border-secondary mb-10"></div>
        </div>
        <div class="flex justify-center items-center mb-20">
          <p
            class="mt-3 text-left text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
          >
            ITS.kompetent ist in 4 Schritte untergliedert. Im ersten Schritt
            wählen Mitarbeiter*innen von KMUs Ihr ITS-Anforderungsprofil aus.
            Danach werden Ihre ITS-Kompetenzen basierend auf dem ausgewählten
            ITS-Anforderungsprofil bestimmt. Jeder ITS-Kompetenztest beinhaltet
            pro ITS- Anforderungsprofil verschiedene IT-sicherheitskritische
            Situationen, die diesen im Arbeitsalltag begegnen können. In diesen
            Situationen werden Mitarbeiter*innen mit bis zu 5 ITS-Bedrohungen
            konfrontiert. Das Verhalten im Umgang mit diesen ITS-Bedrohungen
            wird über 7 ITS- Kompetenzdimensionen gemessen. Im dritten Schritt
            werden umfassende Statistiken zu den Ergebnissen aus der
            ITS-Kompetenzmessung generiert. Zuletzt werden ITS-
            Trainingsempfehlungen vorgeschlagen, die die Lücke zwischen
            IST-Zustand und SOLL-Zustand potentiell schließen können. <br />
            <br />
            <strong
              >Wechseln Sie für eine Erklärung der vier Schritte durch einen
              Klick auf die Zahlen.</strong
            >
          </p>
        </div>

        <Steps
          :activestate="activeStep"
          class="mb-10"
          linecolor="white"
          :choosing-mode="true"
          @changeStep="changeActiveStep"
        ></Steps>
      </div>
    </div>
    <div v-if="activeStep == 1">
      <div class="page-background">
        <div class="standard-container flex flex-col justify-center">
          <h1 ref="innerScrollTarget" class="main-heading pb-10">
            <span class="text-primary xl:inline">ITS-Anforderungsprofil</span>
            {{ " " }}
            <span class="text-secondary xl:inline">bestimmen</span>
          </h1>
          <div class="flex flex-row justify-center items-center">
            <div
              class="border-b-4 rounded-lg w-14 border-secondary mb-10"
            ></div>
          </div>
          <div class="flex justify-center items-center mb-20">
            <p
              class="mt-3 text-left text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
            >
              Im ersten Schritt bestimmen Ihre Mitarbeiter*innen Ihr
              persönliches ITS-Anforderungsprofil. Dazu wählen Sie aus
              {{ jobProfiles.length }} ITS-Anforderungsprofilen. Diese werden im
              Folgenden anhand von Personas erklärt.
            </p>
          </div>
          <div
            class="grid grid-cols-1 lg:grid-cols-2 gap-10 gap-y-20 lg:gap-x-20 xl:gap-x-40"
          >
            <div v-for="jobProfile in jobProfiles" :key="jobProfile.id">
              <transition appear name="fade">
                <job-profile-card
                  :id="jobProfile.id"
                  :name="jobProfile.job_name"
                  :tasks="jobProfile.job_tasks"
                  :description="jobProfile.job_description"
                  :label="jobProfile.id"
                />
              </transition>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeStep == 2">
      <div class="page-background">
        <div class="standard-container flex flex-col justify-center">
          <h1 ref="innerScrollTarget" class="main-heading pb-20">
            <span class="text-primary xl:inline">ITS-Kompetenzen</span>
            {{ " " }}
            <span class="text-secondary xl:inline">messen</span>
          </h1>
          <div class="flex flex-row justify-center items-center">
            <div
              class="border-b-4 rounded-lg w-14 border-secondary mb-10"
            ></div>
          </div>
          <div class="flex justify-center items-center mb-20">
            <p
              class="mt-3 text-left text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
            >
              Im zweiten Schritt bestimmen messen wir die ITS-Kompetenzen Ihrer
              Mitarbeiter*innen. Die ITS-Kompetenzen werden über bis zu 5
              ITS-Bedrohungen gemessen, die in jeweils eine Handlungssituation
              eingebettet sind. Jede ITS-Bedrohun wird über eine Frage zu den 7
              identifizierten ITS-Kompetenzdimensionen ermittelt. Im Folgenden
              stellen wir da, wie wir ITS-Bedrohungen und
              ITS-Kompetenzdimensionen definieren.
            </p>
          </div>
          <explanation-card>
            <template #heading>Was sind ITS-Bedrohungen?</template>
            <template #title
              >ITS-Bedrohungen setzen sich aus ITS-Bedrohungsbereichen und
              ITS-Bedrohungsereignissen zusammen.</template
            >
            <template #content>
              <p class="text-gray-500">
                Als
                <span class="text-secondary font-semibold">
                  ITS-Bedrohungsbereich </span
                >definieren wir jene möglichen Unternehmenswerte (z. B.
                E-Mail-Programm), auf welche die unterschiedlichen
                ITS-Bedrohungsereignisse (z. B. Phishing-Attacke) abzielen
                können.
              </p>
              <p class="text-gray-500">
                Die zweite Dimension
                <span class="text-secondary font-semibold">
                  ITS-Bedrohungsereignis
                </span>
                beinhaltet wiederum Bedrohungsquellen, die potenziell einen
                Schaden an den zuvor erläuterten ITS-Bedrohungsbereichen
                verursachen können.
              </p>
              <p />
              <div class="grid grid-cols-2">
                <div class="mt-5">
                  <h2 class="font-semibold text-primary mb-4">
                    Beispielhafte ITS-Bedrohungsbereiche:
                  </h2>
                  <ul class="pl-4 list-disc text-gray-500">
                    <li>Laptop</li>
                    <li>Mobiltelefon</li>
                    <li>Buchungssystem</li>
                  </ul>
                </div>
                <div>
                  <div class="mt-5">
                    <h2 class="font-semibold text-primary mb-4">
                      Beispielhafte ITS-Bedrohungsereignisse:
                    </h2>
                    <ul class="pl-4 list-disc text-gray-500">
                      <li>Social Engineering</li>
                      <li>Phishing</li>
                      <li>Malware</li>
                    </ul>
                  </div>
                </div>
              </div>
            </template>
            <template #image>
              <img
                src="@/assets/bedrohungen.png"
                class="w-full exportImages"
                alt="Sample image"
              />
            </template>
          </explanation-card>
        </div>
      </div>

      <div class="gradient-background-secondary">
        <div class="standard-container py-20">
          <explanation-card>
            <template #heading>Was sind ITS-Kompetenzen?</template>
            <template #title
              >Unter ITS-Kompetenz verstehen wir die bei Individuen verfügbaren
              (oder erlernbaren) kognitiven Fähigkeiten und Fertigkeiten, um im
              Berufsalltag IT-sicher zu handeln, sowie die damit verbundenen
              motivationalen und sozialen Bereitschaften und Fähigkeiten, um in
              variablen Situationen erfolgreich und verantwortungsvoll eine
              Gefahr abwenden bzw. bewältigen zu können (Weinert 2001). Hierbei
              konnten 7 Dimensionen identifiziert werden, die rechts abgebildet
              sind.</template
            >

            <template #image>
              <img
                :src="require('@/assets/kompetenzdimensionen.png')"
                class="w-full exportImages"
                alt="Sample image"
              />
            </template>
          </explanation-card>
        </div>
      </div>
      <div class="bg-white pt-20 pb-10">
        <div class="standard-container">
          <h1
            class="text-2xl tracking-tight font-extrabold text-primary text-center sm:text-3xl md:text-4xl mb-10"
          >
            ITS-Kompetenzendimensionen
          </h1>

          <div class="flex flex-row justify-center items-center">
            <div
              class="border-b-4 w-14 rounded-lg border-secondary mb-40"
            ></div>
          </div>
          <div
            class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10 lg:gap-20 xl:gap-40 mb-40"
          >
            <div v-for="dimension in competenceDimensions" :key="dimension">
              <Accordion>
                <template #title>{{ dimension.dimension_name }} </template>

                <template #content>{{
                  dimension.dimension_description
                }}</template>
              </Accordion>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeStep == 3">
      <div class="page-background">
        <div class="standard-container flex flex-col justify-center">
          <h1 ref="innerScrollTarget" class="main-heading pb-10">
            <span class="text-primary xl:inline">Statistiken</span>
            {{ " " }}
            <span class="text-secondary xl:inline">erhalten</span>
          </h1>
          <div class="flex flex-row justify-center items-center">
            <div
              class="border-b-4 rounded-lg w-14 border-secondary mb-10"
            ></div>
          </div>
          <div class="flex justify-center items-center mb-20">
            <p
              class="mt-3 text-left text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
            >
              Im dritten Schritt erhalten Ihre Mitarbeiter*innen individuelle
              Statistiken zu den Ergebnissen aus dem ITS-Kompetenztest. Diese
              Statstiken können Sie auf aggregierter Ebene abrufen, sobald Sie
              eine ITS-Kampagne gestartet haben.
            </p>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeStep == 4">
      <div class="page-background">
        <div class="standard-container flex flex-col justify-center">
          <h1 ref="innerScrollTarget" class="main-heading pb-10">
            <span class="text-primary xl:inline"
              >ITS-Trainingsempfehlungen</span
            >
            {{ " " }}
            <span class="text-secondary xl:inline">erhalten</span>
          </h1>
          <div class="flex flex-row justify-center items-center">
            <div
              class="border-b-4 rounded-lg w-14 border-secondary mb-10"
            ></div>
          </div>
          <div class="flex justify-center items-center mb-20">
            <p
              class="mt-3 text-left text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
            >
              Im vierten und letzten Schritt erhalten Ihre Mitarbeiter*innen
              ITS-Trainingsempfehlungen, die zu den individuellen Ergebnissen
              aus dem ITS-Kompetenztest passen. Die untenstehende Abbildung
              zeigt ein Beispiel für das Matching der ITS-Trainings auf
              Mitarbeiter*innenebene.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-if="activeTabId === 'tab3'">
    <div class="page-background">
      <div class="standard-container flex flex-col justify-center">
        <h1 class="main-heading pb-20">
          <span class="text-primary xl:inline">In 3 Schritten</span>
          {{ " " }}
          <span class="text-secondary xl:inline"
            >zur erfolgreichen Kampagne</span
          >
        </h1>
        <div class="flex flex-row justify-center items-center">
          <div class="border-b-4 rounded-lg w-14 border-secondary mb-10"></div>
        </div>
        <div class="flex justify-center items-center mb-20">
          <p
            class="mt-3 text-left text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
          >
            Um erfolgreich eine Kampagne für Ihr KMU abzusolvieren, folgen Sie
            drei Schritten. Im ersten Schritt initiieren Sie die Kampagne und
            laden die Mitarbeiter*innen Ihres KMUs ein. Dazu haben Sie zwei
            Optionen. Sie können entweder einen Einladungs-Code generieren, den
            alle Mitarbeiter*innen nutzen. Alternativ können Sie für jeden
            Mitarbeitenden einen separaten Einladungs-Code genrieren. Im zweiten
            Schritt führen Ihre Mitarbeiter*innen den ITS-Kompetenztest
            basierend auf Ihrem gewahlten ITS-Anforderungsprofil durch. Darauf
            basierend zeigen wir Ihnen im dritten Schritt umfassende Statistiken
            zu den Ergebnissen der ITS-Kompetenzmessung. Diese Ergebnisse können
            Sie exportieren und erhalten einen Mangement Report, der weitere
            Handlungsempfehlungen ausgibt.
          </p>
        </div>

        <StepsCampagne class="mb-40" linecolor="white"></StepsCampagne>
      </div>
    </div>
  </div>
</template>

<script>
import ExplanationCard from "@/components/dashboard/ExplanationCard.vue";
import Hero from "@/components/base/Hero.vue";
import Accordion from "@/components/base/Accordion.vue";
import IconCard from "@/components/base/IconCard.vue";
import Steps from "@/components/base/Steps.vue";
import StepsCampagne from "@/components/campagne/StepsCampagne.vue";

import JobProfileCard from "@/components/profile/JobProfileCard.vue";

import { useJobProfileStore } from "@/store/JobProfileStore";
import { useCompetenceTestStore } from "@/store/CompetenceTestStore";

import { MagnifyingGlassIcon } from "@heroicons/vue/20/solid";
import { ChartBarIcon } from "@heroicons/vue/20/solid";
import { DocumentChartBarIcon } from "@heroicons/vue/20/solid";
import { ShieldCheckIcon } from "@heroicons/vue/20/solid";
export default {
  components: {
    ExplanationCard,
    Hero,
    IconCard,
    Accordion,
    Steps,
    StepsCampagne,
    JobProfileCard,
    MagnifyingGlassIcon,
    ChartBarIcon,
    DocumentChartBarIcon,
    ShieldCheckIcon,
  },
  /**
   * Initializes and returns the state for the Vue component using composition API.
   *
   * This setup function utilizes the Vuex stores specific to job profiles and competence tests.
   * It invokes `useJobProfileStore` to access and manage the state related to job profiles,
   * and `useCompetenceTestStore` for managing state related to competence tests. The function
   * then returns these stores for use within the Vue component, enabling reactive state management
   * and encapsulation of business logic associated with job profiles and competence tests.
   *
   * @returns {Object} An object containing references to `jobProfileStore` and `competenceTestStore`.
   */
  setup() {
    const jobProfileStore = useJobProfileStore();
    const competenceTestStore = useCompetenceTestStore();

    return {
      jobProfileStore,
      competenceTestStore,
    };
  },
  data() {
    return {
      modalOpen: false,
      activeStep: 1,
      activeTabId: "tab1",
      isInnerTabActive: false, // New property to track inner tab activation
      jobProfiles: [],
      tabs: [
        { id: "tab1", text: "Was ist ITS.kompetent?" },
        { id: "tab2", text: "Wie funktioniert ITS.kompetent?" },
        { id: "tab3", text: "Welche Funktionen bietet das KMU-Management?" },
      ],

      emails: [],
      competenceDimensions: [],
    };
  },

  /**
   * A Vue component lifecycle method that is called after data changes and the DOM is re-rendered.
   * This method is used to adjust CSS variables and handle scroll behavior based on tab activation.
   *
   * It sets a CSS variable `--min-slide-height` based on the viewport height to control the minimum
   * height of slides. After DOM updates, it checks the current tab state and performs scrolling to
   * ensure that the correct tab content is in view.
   */
  updated() {
    const vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty("--min-slide-height", `${vh}px`);

    this.$nextTick(() => {
      if (this.activeTabId === "tab2" && !this.isInnerTabActive) {
        this.$refs.scrollTarget?.scrollIntoView();
      } else if (this.isInnerTabActive) {
        this.$refs.innerScrollTarget?.scrollIntoView();
      } else {
        this.$refs.scrollTarget?.scrollIntoView();
      }
    });
  },

  /**
   * A Vue component lifecycle method that runs once the component is mounted to the DOM.
   * It asynchronously fetches job profiles and competence dimensions from their respective stores.
   *
   * This method is critical for initializing the component with data required for rendering
   * job profiles and competence dimensions, fetched asynchronously from Vuex stores immediately
   * after the component has been rendered to the DOM.
   */
  async mounted() {
    this.jobProfiles = await this.jobProfileStore.getJobProfiles();
    this.competenceDimensions =
      await this.competenceTestStore.getCompetenceDimensions();
  },

  methods: {
    /**
     * Changes the active tab based on user interaction.
     * This method resets the inner tab active state whenever a new tab is selected.
     *
     * @param {string} tab - The identifier of the tab to activate.
     */
    changeTab(tab) {
      this.activeTabId = tab;
      this.isInnerTabActive = false;
    },

    /**
     * Activates an inner tab within a larger tabbed interface, typically called when an inner tab is clicked.
     * This method sets the active step for the inner content and marks the inner tab as active.
     *
     * @param {string} activeStep - The identifier of the step within an inner tab to activate.
     */
    changeActiveStep(activeStep) {
      this.isInnerTabActive = true;
      this.activeStep = activeStep;
    },
  },
};
</script>

<style scoped>
.fade-enter-from {
  opacity: 0;
}
.fade-enter-active {
  transition: all 2s ease;
}
</style>
