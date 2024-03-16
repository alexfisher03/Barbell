document.addEventListener("DOMContentLoaded", () => {
    document.getElementById('toggleMembersDropdown').addEventListener('click', () => {
        document.getElementById('membersDropdown').classList.toggle("hidden");
    });
});