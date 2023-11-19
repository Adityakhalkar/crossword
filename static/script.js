// Get the button element
const startButton = document.querySelector('#start-button');
const okbutton = document.querySelector('#ok');

function toggleBlur(blur) {
    // Get all elements with the blurred class
    const blurredElements = document.querySelectorAll('.blurred');

    // Toggle the blur class for each element based on the blur parameter
    blurredElements.forEach(element => {
        if (blur) {
            element.classList.add('blurred');
        } else {
            element.classList.remove('blurred');
        }
    });
}

function closePopup() {
    const popup = document.getElementById('custom-popup');
    popup.style.display = 'none';
    toggleBlur(false);  // Unblur the elements
}

function openPopup() {
    const popup = document.getElementById('custom-popup');
    popup.style.display = 'block';
    toggleBlur(true);  // Blur the elements
}

// Add a click event listener to the button
okbutton.addEventListener('click', () => {
    // Show the custom pop-up to start the game

    // Get the timer element
    const timerElement = document.querySelector('#timer');

    // Set the initial time to 0
    let second = 0;
    let minute = 0;
    let timeElapsed = 0;

    // Update the timer element every second
    const timerInterval = setInterval(() => {
        // Update the timer element with the new time
        timerElement.textContent = `${String(minute).padStart(2, '0')}:${String(second).padStart(2, '0')}`;
        timeElapsed++;
        // Increment the time
        second++;

        // Check if 60 seconds have passed
        if (second === 60) {
            second = 0;
            minute++;
        }

        // If you want to add a stopping condition, you can do it here based on your requirements.
        // For example, if (minute === 10) { clearInterval(timerInterval); closePopup(); }
    }, 1000);
});
