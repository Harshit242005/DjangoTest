const jwt = require('jsonwebtoken');
const secretKey = 'token';

function generateToken(userId, expiresInMinutes) {
  const expirationTime = expiresInMinutes * 60; // Convert minutes to seconds
  const token = jwt.sign({ userId }, secretKey, { expiresIn: expirationTime });
  return token;
}

// Example: Generate a token with a variable expiration time of 30 minutes
const userToken = generateToken(123, 30);
console.log(userToken);