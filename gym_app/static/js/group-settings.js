document.addEventListener("DOMContentLoaded", () => {
    document.getElementById('toggleMembersDropdown').addEventListener('click', () => {
        document.getElementById('membersDropdown').classList.toggle("hidden");
    });
    document.getElementById('removeButton').addEventListener('click', event =>
    {
        document.getElementById('groupSettingsForm').submit();
    });
});