const requestDemo = document.querySelector('.request');
const formContainer = document.querySelector('.form-container');
const overlay = document.getElementById('overlay');
const demoForm = document.querySelector('#demo-form');
const emailForm = document.querySelector('#email');
const submitButton = document.querySelector('#submit-button');


const newsletterForm= document.querySelector('.newsletter-form');
const newsInfo = document.querySelector('.news-info');
const emailButton = document.querySelector('.email-button');







requestDemo.addEventListener('click', function(e) {
    formContainer.style.display = 'block';
    overlay.style.display = 'block';
    requestDemo.disabled = true;
});

demoForm.addEventListener('submit', function(e) {
    e.preventDefault();

    if (emailForm.value) {
        
        formContainer.style.display = 'none';
        overlay.style.display = 'none';

        console.log('Email successfully submitted');
        alert('Email successfully submitted');
        demoForm.reset();
        requestDemo.disabled = false;
    }
});

function closeForm() {
    formContainer.style.display = 'none';
    overlay.style.display = 'none';
    demoForm.reset();
    requestDemo.disabled = false;
}

function showForm() {
    formContainer.style.display = 'block';
    overlay.style.display = 'block';
    requestDemo.disabled = true;
}

newsletterForm.addEventListener('submit', function(e){
    e.preventDefault();
    newsInfo.innerHTML='Thanks for the support';
    newsletterForm.reset()

})










