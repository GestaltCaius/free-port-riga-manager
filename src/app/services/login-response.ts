export enum LoginStatus {
    SUCCESS = 'Login success',
    FAIL = 'Login failed',
}

export class LoginResponse {
    message: LoginStatus;
    access_token: string;
    refresh_token: string;
}