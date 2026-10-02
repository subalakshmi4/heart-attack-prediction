const predictionForm = document.getElementById("predictionForm");
const result = document.getElementById("result");

predictionForm.addEventListener("submit", async function (event) {
  event.preventDefault();

  const patientData = {
    age: Number(document.getElementById("age").value),
    gender: Number(document.getElementById("gender").value),
    heart_rate: Number(document.getElementById("heartRate").value),
    systolic_blood_pressure: Number(
      document.getElementById("systolicBP").value,
    ),
    diastolic_blood_pressure: Number(
      document.getElementById("diastolicBP").value,
    ),
    blood_sugar: Number(document.getElementById("bloodSugar").value),
    ck_mb: Number(document.getElementById("ckmb").value),
    troponin: Number(document.getElementById("troponin").value),
  };

  result.textContent = "Making prediction...";

  try {
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(patientData),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Prediction failed.");
    }

    result.textContent = data.prediction;
  } catch (error) {
    result.textContent = "Unable to connect to the prediction server.";
    console.error(error);
  }
});
