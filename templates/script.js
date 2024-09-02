document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    let username = document.getElementById('username').value;
    let email = document.getElementById('email').value;

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({username: username, email: email})
    }).then(response => {
        if (response.ok) {
            window.location.href = '/view_data'; // Redirect to view data page
        } else {
            alert('Failed to submit data.');
        }
    });
});