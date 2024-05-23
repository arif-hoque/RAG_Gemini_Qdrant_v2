<script setup>
import { ref, unref } from "vue";

const question = ref("");
const response = ref("");
const resultData = ref("");
const responseLoading = ref(false);

const fetchResponse = async () => {
  try {
     // Clear the resultData at the beginning
    resetField();
    console.log(unref(question)); // Log the question value
    responseLoading.value = true;
    const res = await fetch("http://0.0.0.0:8000/query", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question: unref(question) }),
    });
    console.log("Response object:", res); // Log the Response object
    responseLoading.value = false;
    if (!res.ok) {
      throw new Error(`HTTP error ${res.status}`);
    }

    const data = await res.json();
    console.log("Response data:", data[0],res); // Log the response data
    resultData.value = data[0].response; // Assign the response text to the resultData ref
  } catch (error) {
    console.error("Error fetching data:", error);
    responseLoading.value = false;

  }
};
const resetField = () => {
  resultData.value = "";
};
</script>

<template>
  <v-container class="d-flex justify-center align-center fill-height" fluid>
    <div>
      <div class="image mb-4">
        <img :width="300" aspect-ratio="16/9" src="./assets/logo.png"></img>
      </div>
      <v-textarea v-model="question" label="Enter your question" variant="outlined"></v-textarea>
      <div class="button-container">
        <span v-if="responseLoading">
          <v-progress-circular color="primary" indeterminate></v-progress-circular>
        </span>
        <v-btn v-else @click="fetchResponse" class="ask-button"> Ask </v-btn>
      </div>
      <div class="result-container">
        <v-textarea v-model="resultData" label="Response" variant="outlined" readonly></v-textarea>
      </div>
    </div>
  </v-container>
</template>


<style scoped>
.fill-height {
  height: 100vh;
}

.image {
  margin-top: 200px;
  margin-bottom: 20px;
  margin-left: 250px;
}

.result-container {
  margin-top: 20px;
  /* Add some spacing between the button and the result area */
  width: 800px;
}

.button-container {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
  /* Add margin below the button */
}

.ask-button {
  margin: 0;
  /* Reset margin for the button */
}
</style>