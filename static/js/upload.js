window.onload = function() {
    function handleFileUpload(event) {
        var file = event.target.files[0];
        var reader = new FileReader();
        reader.onload = function(e) {
            var typedArray = new Uint8Array(e.target.result);
            pdfjsLib.getDocument({data: typedArray}).promise.then(function(pdf) {
                var numPages = pdf.numPages;
                var promises = [];
                for (var i = 1; i <= numPages; i++) {
                    promises.push(pdf.getPage(i).then(function(page) {
                        return page.getTextContent();
                    }).then(function(textContent) {
                        var text = textContent.items.map(function(item) {
                            return item.str;
                        }).join(' ');
                        console.log('Page text:', text);  // Log the text of each page
                        return text;
                    }));
                }
                Promise.all(promises).then(function(texts) {
                    var fullText = texts.join('\n');
                    console.log('Full text:', fullText);  // Log the full text
                    document.getElementById('essay_box').value = fullText;
                });
            });
        };
        reader.readAsArrayBuffer(file);
    }

    // Attach the handleFileUpload function to the onchange event of the file input
    document.getElementById('uploadButton').addEventListener('change', handleFileUpload);


    // Get the forms and the textareas
    var dataForm = document.getElementById('dataForm');
    var secondForm = document.getElementById('secondForm');
    var claimBox = document.getElementById('claim_box');
    var essayBox = document.getElementById('essay_box');

    // Add an event listener for the submit event of the forms
    dataForm.addEventListener('submit', function(event) {
        // If the textarea is empty, prevent the form from being submitted
        if (claimBox.value.trim() === '') {
            event.preventDefault();
            alert('Please enter a claim before submitting.');
        }
    });

    secondForm.addEventListener('submit', function(event) {
        // If the textarea is empty, prevent the form from being submitted
        if (essayBox.value.trim() === '') {
            event.preventDefault();
            alert('Please upload an essay before submitting.');
        }
    });
}