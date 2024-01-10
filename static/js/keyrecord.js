window.addEventListener('keydown', function(event) {
    // Check if the key pressed was the space bar
    if (event.code === 'Space') {
        // Check if the focus is in a text area
        if (document.activeElement.tagName.toLowerCase() === 'textarea') {
            return; // If it is, don't start the recording
        }

        // Prevent the default action to stop the page from scrolling
        event.preventDefault();

        // Start the recording
        startRecording();
    }
});

window.addEventListener('keyup', function(event) {
    // Check if the key released was the space bar
    if (event.code === 'Space') {
        // Check if the focus is in a text area
        if (document.activeElement.tagName.toLowerCase() === 'textarea') {
            return; // If it is, don't stop the recording
        }

        // Stop the recording
        stopRecording();
    }
});