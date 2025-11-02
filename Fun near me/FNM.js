const Email = document.getElementById('mail');
const mailtag = document.getElementById('mailtag');

Email.addEventListener('focus', () => {
mailtag.style.display = 'block';
mailtag.classList.add('Emailtag');
});

Email.addEventListener('blur', () => {
mailtag.classList.remove('Emailtag');
mailtag.style.display = 'none';
});


const pass = document.getElementById('pass');
const password = document.getElementById('password');

pass.addEventListener('focus', () => {
password.style.display = 'block';
password.classList.add('passtag');
});

pass.addEventListener('blur', () => {
password.classList.remove('passtag');
password.style.display = 'none';
});