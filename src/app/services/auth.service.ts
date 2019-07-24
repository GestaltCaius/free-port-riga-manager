import { Injectable } from '@angular/core';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { User } from './user';
import { LoginResponse } from './login-response';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private BASE_URL: string = 'http://localhost:5000/auth';


  constructor(private http: HttpClient) { }

  login(user: User): void {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
      })
    };

    let url: string = `${this.BASE_URL}/login`;
    this.http.post<LoginResponse>(url, user, httpOptions).subscribe(
      loginResponse => {
        localStorage.setItem('jwt_access_token', loginResponse.access_token);
        localStorage.setItem('jwt_refresh_token', loginResponse.refresh_token);
      },
      err => console.log('error') // TODO
    );
  }

  isLoggedIn(): Observable<string> {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
        'Authorization': localStorage.getItem('jwt_access_token'),
      })
    };
    return this.http.get<string>('${this.BASE_URL}/isloggedin', httpOptions)
  }
}
