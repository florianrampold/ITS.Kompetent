<template>
  <Hero
    ><template #title>
      <h1 class="main-heading">
        <span class="text-primary xl:inline">Nehmen Sie <br /> </span>
        {{ " " }}
        <span class="text-secondary xl:inline">Kontakt zu uns auf</span>
      </h1></template
    >
    <template #content>
      <p
        class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
      >
        Sie möchten an ITS.Kompetent als KMU teilnehmen? Wir freuen uns über
        Ihre Kontaktaufnahme!
      </p></template
    >
    >

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
    <div class="page-background">
      <div class="standard-container flex flex-col items-center justify-center">
        <h1 class="main-heading pb-20">
          <span class="text-primary xl:inline">Kontakt </span>
          {{ " " }}
          <span class="text-secondary xl:inline">zu uns aufnehmen</span>
        </h1>
        <div class="flex flex-row justify-center items-center">
          <div class="border-b-4 rounded-lg w-14 border-secondary mb-10"></div>
        </div>
        <div class="flex justify-center items-center mb-20">
          <p
            class="mt-3 text-left text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
          >
            Wenn Sie Interesse daran haben mit Ihrem KMU an ITS.kompetent
            teilzunehmen, senden Sie uns eine kurze Nachricht über das
            Kontaktformular. Wir kommen auf Sie zurück mit den Details.
          </p>
        </div>
        <div class="bg-white rounded-lg shadow-lg p-10 w-3/4">
          <Form class="grid grid-cols-2" @submit="sendEmail">
            <div class="flex flex-col text-left col-span-2 justify-start">
              <Field
                v-model="name"
                :validate-on-input="true"
                name="name"
                rules="required"
                type="text"
                class="w-full outline-none border focus:border-primary text-primary text-sm font-semibold py-4 px-8 rounded-lg mb-4 mr-2"
                placeholder="Ihr Name"
              />
              <ErrorMessage
                name="name"
                class="text-red-600 text-xs font-bold mb-5 pl-4"
              />
            </div>
            <div class="col-span-2 flex flex-col text-left justify-start">
              <Field
                v-model="emailMessage"
                rules="required|email"
                :validate-on-input="true"
                name="emailMessage"
                type="email"
                class="w-full outline-none border focus:border-primary text-primary text-sm font-semibold py-4 px-8 rounded-lg mb-4"
                placeholder="Email-Addresse"
              />
              <ErrorMessage
                name="emailMessage"
                class="text-red-600 text-xs font-bold mb-5 pl-4"
              />
            </div>
            <div class="col-span-2 flex flex-col text-left justify-start">
              <Field
                v-model="message"
                :validate-on-input="true"
                name="message"
                rules="required"
                as="textarea"
                class="w-full outline-none col-span-2 border focus:border-primary text-primary text-sm font-semibold py-4 px-8 rounded-lg mb-4"
                placeholder="Nachricht"
              />
              <ErrorMessage
                name="message"
                class="text-red-600 text-xs font-bold mb-5 pl-4"
              />
            </div>
            <div class="col-span-2 flex justify-center">
              <button class="btn-primary" type="submit">Absenden</button>
            </div>
          </Form>
        </div>
      </div>
    </div>
  </div>
  <div v-if="activeTabId === 'tab2'">
    <div class="page-background">
      <div class="standard-container flex flex-col items-center justify-center">
        <h1 class="main-heading pb-20">
          <span class="text-primary xl:inline">ITS.kompetent</span>
          {{ " " }}
          <span class="text-secondary xl:inline">aufsetzen</span>
        </h1>
        <div class="flex flex-row justify-center items-center">
          <div class="border-b-4 rounded-lg w-14 border-secondary mb-10"></div>
        </div>
        <div class="flex justify-center items-center mb-20">
          <p
            class="mt-3 text-left text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
          >
            Nach erfolgreiche Kontaktaufnahme zu uns, erhalten Sie eine Instanz
            von ITS.kompetent, die sie bequem über Docker in Ihrem internen
            Unternehmensnetzwerk aufsetzen können. Zudem erhalten Sie eine
            Schritt-für-Schritt Anleitung, die Sie bei der Aufsetzung von
            ITS.kompetent unterstütz.
          </p>
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

  <PopUp
    v-if="successPopUp"
    type="success"
    title="Nachricht gesendet"
    content="Ihre Nachricht wurde erfolgreich gesendet!"
    @popup-closed="successPopUp = false"
  />
  <PopUp
    v-if="failedPopUp"
    type="danger"
    title="Nachricht senden gescheitert"
    content="Das hat leider nicht geklappt. Überprüfen Sie Bitte Ihre Eingaben!"
    @popup-closed="failedPopUp = false"
  />
</template>

<script>
import Hero from "@/components/base/Hero.vue";
import StepsCampagne from "@/components/campagne/StepsCampagne.vue";
import { useCompetenceTestStore } from "@/store/CompetenceTestStore.js";

import { Field, Form, ErrorMessage } from "vee-validate";
import { defineRule } from "vee-validate";
import { required, email } from "@vee-validate/rules";
import { configure } from "vee-validate";
configure({
  generateMessage: (context) => {
    switch (context.field) {
      case "name":
        return "Sie müssen einen Namen eingeben.";
      case "emailMessage":
        return "Sie müssen eine gültige E-Mail-Adresse eingeben.";
      case "message":
        return "Sie müssen eine Nachricht eingeben.";
    }
  },
});
defineRule("required", required);
defineRule("email", email);

export default {
  components: {
    Hero,
    StepsCampagne,
    Field,
    Form,
    ErrorMessage,
  },
  setup() {
    const competenceTestStore = useCompetenceTestStore();

    return { competenceTestStore };
  },
  data() {
    return {
      successPopUp: false,
      failedPopUp: false,
      name: "",
      emailMessage: "",
      message: "",
      activeTabId: "tab1",
      tabs: [
        { id: "tab1", text: "Kontakt aufnehmen" },
        { id: "tab2", text: "ITS.kompetent aufsetzen" },
        { id: "tab3", text: "Kampagne erstellen" },
      ],
    };
  },

  methods: {
    /**
     * Sends an email using the provided form data.
     *
     * @returns {Promise<void>} A promise that resolves after the email is sent successfully or rejects if there is an error.
     */
    async sendEmail() {
      let formData = new FormData();
      formData.append("from", this.name);
      formData.append("email", this.emailMessage);
      formData.append("message", this.message);
      try {
        let response = await this.competenceTestStore.sendContactRequest(
          formData
        );
        console.log(response.data);
        this.successPopUp = true;
      } catch (error) {
        this.failedPopUp = true;
        console.log(error.response.data);
      }
    },

    /**
     * Changes the active tab to the specified tab.
     *
     * @param {string} tab The identifier of the tab to switch to.
     */
    changeTab(tab) {
      this.activeTabId = tab;
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
