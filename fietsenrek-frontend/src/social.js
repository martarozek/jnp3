export default socialConfig;

function socialConfig($authProvider) {
  $authProvider.baseUrl = 'http://localhost:9999';
  $authProvider.signupUrl = '/rest-auth/registration/';
  $authProvider.loginUrl = '/rest-auth/login/';
  $authProvider.facebook({
    clientId: '237608516653103',
    url: 'http://localhost:9999/rest-auth/facebook/'
  });
}
