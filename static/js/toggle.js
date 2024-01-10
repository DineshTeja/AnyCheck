// JavaScript to toggle between forms
document.getElementById('toggleButton').addEventListener('click', function() {
    var dataForm = document.getElementById('dataForm');
    var secondForm = document.getElementById('secondForm');
    
    // Toggle display of the forms
    if (dataForm.style.display === 'none') {
        dataForm.style.display = 'block';
        secondForm.style.display = 'none';
    } else {
        dataForm.style.display = 'none';
        secondForm.style.display = 'block';
    }
});

// Display the correct form based on the variable passed from Flask
var form = document.body.getAttribute('data-form');
if (form == 'secondForm') {
    document.getElementById('dataForm').style.display = 'none';
    document.getElementById('secondForm').style.display = 'block';
}
else if (form == 'dataForm') {
    document.getElementById('dataForm').style.display = 'block';
    document.getElementById('secondForm').style.display = 'none';
}