<?php
session_start();

// Verificar si el usuario ha enviado el formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Verificar las credenciales (aquí debes implementar tu lógica de autenticación)
    $username = $_POST['godcat2'];
    $password = $_POST['Godcat_123'];

    // Por ejemplo, supongamos que el usuario es válido si el nombre de usuario es "admin" y la contraseña es "admin123"
    if ($username === 'godcat2' && $password === 'Godcat_123') {
        // Autenticación exitosa, establecer una variable de sesión para indicar que el usuario está autenticado
        $_SESSION['authenticated'] = true;

        // Redirigir al usuario a otro archivo PHP
        header("Location: server.php");
        exit();
    } else {
        // Autenticación fallida, mostrar un mensaje de error
        $error_message = "Credenciales inválidas. Inténtalo de nuevo.";
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Form</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css">
    <style>
        /* Estilos omitidos por brevedad */
    </style>
</head>
<body>

<main class="form-signin">
    <form id="loginForm" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <h1 class="h3 mb-3 fw-normal">Login Form</h1>

        <?php if(isset($error_message)): ?>
        <div class="alert alert-danger" role="alert">
            <?php echo $error_message; ?>
        </div>
        <?php endif; ?>

        <div class="form-floating">
            <input type="text" class="form-control" id="username" name="godcat2" placeholder="Username" required>
            <label for="username">Username</label>
        </div>
        <div class="form-floating">
            <input type="password" class="form-control" id="password" name="Godcat_123" placeholder="Password" required>
            <label for="password">Password</label>
        </div>

        <div class="form-check text-start my-3">
            <input class="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault">
            <label class="form-check-label" for="flexCheckDefault">Remember me</label>
        </div>

        <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
    </form>
</main>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>

