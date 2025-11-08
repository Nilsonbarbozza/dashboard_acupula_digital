export default function handler(req, res) {
  const password = "raphaelli3332"; // ALTERE SUA SENHA AQUI
  const cookie = req.cookies?.auth;

  // Se já tem cookie de autenticação → libera acesso
  if (cookie === password) {
    return res.next();
  }

  // Se a rota é a tela de senha → deixa passar
  if (req.url.includes("password.html")) {
    return res.next();
  }

  // Senão → redireciona para tela de senha
  return res.redirect("/password.html");
}
