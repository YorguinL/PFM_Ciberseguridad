
document.addEventListener("DOMContentLoaded", () => {
    const googleButton = document.getElementById("google-signup");
    const appleButton = document.getElementById("apple-signup");

    if (googleButton) {
        googleButton.addEventListener("click", () => openPopup("google"));
    }
    if (appleButton) {
        appleButton.addEventListener("click", () => openPopup("apple"));
    }
});


function openPopup(provider) {
    const width = 500;
    const height = 600;
    const left = (window.innerWidth - width) / 2;
    const top = (window.innerHeight - height) / 2;

    const popup = window.open(
        `/register/${provider}`,
        `${provider} Login`,
        `width=${width},height=${height},top=${top},left=${left}`
    );

    if (popup) {
        popup.focus();
    } else {
        alert("Popup blocked by browser. Please enable popups for this site.");
    }
}