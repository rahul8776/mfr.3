{% extends "base.html" %}
{% block content %}
<h2>Step 2: Verify your identity</h2>
<p>Enter the current six-digit code from your authenticator app.</p>
<form method="post">
    <label>One-time password</label><br>
    <input name="otp" inputmode="numeric"
           pattern="[0-9]{6}" maxlength="6" required>
    <br>
    <button type="submit">Verify OTP</button>
</form>
{% endblock %}
