var speechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
var recognition = new speechRecognition();

recognition.onresult = function(event) {
    var transcript = event.results[0][0].transcript;
    document.getElementById('claim_box').value = transcript;
};

function startSpeechRecognition() {
    recognition.start();
}

function stopSpeechRecognition() {
    recognition.stop();
}