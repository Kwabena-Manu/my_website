document.addEventListener("DOMContentLoaded", function () {
    const resumeButton = document.querySelectorAll(".resume-button");
    const contactForm = document.getElementById('contactForm');
    const nameInput = document.getElementById('nameInput');
    const messageInput = document.getElementById('messageInput');
    const formMessage = document.getElementById('formMessage');



    console.log(resumeButton);
    if (resumeButton.length > 0) {
        resumeButton.forEach(resbut => {

            resbut.addEventListener("click", function (event) {
                event.preventDefault();
                window.location.href = "/static/mywebsite/files/Kwabena-Manu-Resume-2025-11.pdf";
            });
        });
    }

    const myEmailAddress = 'kwabenamanu61@yahoo.com';

    if (contactForm) {
        contactForm.addEventListener('submit', function (event) {
            event.preventDefault();

            formMessage.innerHTML = '';
            formMessage.classList.remove('text-success', 'text-danger');

            const name = nameInput.value.trim();
            const message = messageInput.value.trim();

            if (!name || !message) {
                formMessage.textContent = 'Please fill in your name and message.';
                formMessage.classList.add('text-danger');
                return;
            }


            const subject = encodeURIComponent(`Message from ${name} via your website`);
            const body = encodeURIComponent(`Hi,\n\nMy name is ${name}.\n\nMessage:\n${message}\n\n`);

            const mailtoLink = `mailto:${myEmailAddress}?subject=${subject}&body=${body}`;

            window.location.href = mailtoLink;

            formMessage.textContent = 'Your email client should open shortly!';
            formMessage.classList.add('text-success');
            contactForm.reset();
        });
    }



});