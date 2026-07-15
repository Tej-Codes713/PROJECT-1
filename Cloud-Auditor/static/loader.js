document.addEventListener("DOMContentLoaded", () => {

    const loadingScreen = document.getElementById("loading-screen");
    const progressBar = document.getElementById("progress-bar");
    const progressText = document.getElementById("progress-text");
    const statusText = document.getElementById("status-text");
    const dashboard = document.getElementById("dashboard-content");

    const steps = [
        { percent: 20, text: "Scanning EC2 Instances..." },
        { percent: 40, text: "Scanning EBS Volumes..." },
        { percent: 60, text: "Scanning Elastic IPs..." },
        { percent: 80, text: "Scanning IAM Users..." },
        { percent: 100, text: "Generating Dashboard..." }
    ];

    let index = 0;

    function nextStep() {

        if (index >= steps.length) {

            loadingScreen.style.opacity = "0";

setTimeout(() => {

    loadingScreen.style.display = "none";

    dashboard.style.display = "block";

}, 400);

            return;
        }

        progressBar.style.width = steps[index].percent + "%";
        progressText.innerHTML = steps[index].percent + "%";
        statusText.innerHTML = steps[index].text;

        index++;

        setTimeout(nextStep, 700);

    }

    dashboard.style.display = "none";

    nextStep();

});