<template>
  <div class="bg-primary">
    <div class="standard-container h-full p-10">
      <div class="flex flex-wrap items-center justify-center text-neutral-800">
        <div class="w-full">
          <div class="block rounded-lg bg-white shadow-lg dark:bg-neutral-800">
            <div class="g-0 lg:flex lg:flex-wrap">
              <!-- Left column container-->
              <div class="px-4 md:px-0 lg:w-6/12">
                <div class="md:mx-6 md:p-12">
                  <!--Logo-->
                  <div class="text-center">
                    <img
                      class="mx-auto py-4"
                      src="@/assets/ITS_Kompetent_Logo.svg"
                      alt="logo"
                    />
                    <h4
                      class="my-12 mt-10 pb-1 text-xl xl:text-4xl font-semibold"
                    >
                      KMU-Management Login
                    </h4>
                  </div>

                  <Form class="flex-col" @submit="handleSubmit">
                    <div class="flex-col text-left justify-start">
                      <Field
                        v-model="identifier"
                        :validate-on-input="true"
                        name="identifier"
                        rules="required"
                        type="text"
                        class="w-full outline-none border focus:border-primary text-primary text-sm font-semibold py-4 px-8 rounded-lg mb-2 mr-2"
                        placeholder="Benutzername"
                      />
                      <ErrorMessage
                        name="identifier"
                        class="text-red-600 text-xs font-bold pb-5"
                      />
                    </div>
                    <div class="flex-col text-left justify-start">
                      <Field
                        v-model="password"
                        :validate-on-input="true"
                        name="password"
                        type="password"
                        rules="required"
                        class="w-full outline-none border focus:border-primary text-primary text-sm font-semibold py-4 px-8 rounded-lg mb-2"
                        placeholder="Passwort"
                      />
                      <ErrorMessage
                        name="password"
                        class="text-red-600 text-left text-xs font-bold pb-5"
                      />
                    </div>

                    <div
                      class="col-span-2 pt-5 my-5 flex justify-center items-center"
                    >
                      <button class="btn-primary" type="submit">
                        Einloggen
                      </button>
                    </div>
                  </Form>
                </div>
              </div>

              <!-- Right column container with background and description-->
              <div
                class="flex items-center justify-center bg-gray-200 rounded-b-lg lg:w-6/12 lg:rounded-r-lg lg:rounded-bl-none"
              ></div>
            </div>
          </div>
        </div>
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
    title="Login gescheitert"
    :content="popUpContent"
    @popup-closed="failedPopUp = false"
  />
</template>

<script>
import { useAuthStore } from "@/store/AuthStore";
import { passwordChangeURL } from "@/config.js";

import { Field, Form, ErrorMessage } from "vee-validate";
import { defineRule } from "vee-validate";
import { required, email } from "@vee-validate/rules";
import { configure } from "vee-validate";
configure({
  generateMessage: (context) => {
    switch (context.field) {
      case "identifier":
        return "Sie müssen einen Benutzernamen eingeben.";
      case "password":
        return "Sie müssen ein Passwort eingeben.";
      case "message":
        return "Sie müssen eine Nachricht eingeben.";
      default:
        return `Das Feld ${context.field} ist ungültig`;
    }
  },
});
defineRule("required", required);
defineRule("email", email);

export default {
  components: {
    Field,
    Form,
    ErrorMessage,
  },
  data() {
    return {
      successPopUp: false,
      failedPopUp: false,
      popUpContent: "",
      identifier: "",
      password: "",
    };
  },

  methods: {
    /**
     * A method that tries to log in users. The log in is for campagane managers and redirects them to the campagne management portal (self-service-portal).
     * @throws {Error} Throws various errors depending on the error response of the API.
     *
     */
    async handleSubmit() {
      const authStore = useAuthStore();
      await authStore.ensureCsrfToken();

      authStore
        .login({
          username: this.identifier,
          password: this.password,
        })
        .then(() => {
          // Login successful, perform any necessary redirection or actions
          this.checkPasswordChange();
        })
        .catch((error) => {
          // Handle login error
          if (error.response && error.response.status === 403) {
            this.popUpContent =
              "Ex exisitiert ein Account, aber sie besitzen nicht die notwendigen Rechte sich hier anzumelden. Kontaktieren Sie Ihren Administrator!";
            //this.checkPasswordChange();
          } else if (error.response && error.response.status === 401) {
            this.popUpContent =
              "Ihr Benutzername oder Passwort ist nicht korrekt. Überprüfen Sie Bitte Ihre Eingaben!";
          } else {
            this.popUpContent =
              "Das hat leider nicht geklappt. Wenden Sie sich bitte an Ihren Administrator oder versuchen Sie es später erneut!";
          }

          this.failedPopUp = true;
        });
    },

    checkPasswordChange() {
      const authStore = useAuthStore();

      authStore
        .checkPasswordChange()
        .then((response) => {
          if (response.must_change_password) {
            // Redirect to the Django password change page
            //window.location.href = '/accounts/password_change/';
            this.navigateToPasswordReset();
          } else {
            // Proceed with the normal flow, e.g., redirect to the dashboard
            this.$router.push({
              name: "SelfServicePortal",
            });
          }
        })
        .catch((error) => {
          console.error("Error checking password change status:", error);
        });
    },
    /**
     * A method that triggers the changing of the password. Navigates to API password change endpoints.
     *
     */
    navigateToPasswordReset() {
      window.open(`${passwordChangeURL}/accounts/password_change/`, "_self");
    },
  },
};
</script>
