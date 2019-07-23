import { Injectable } from '@angular/core';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { User } from './user';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private BASE_URL: string = 'http://localhost:5000/auth';

  private httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json',
      'Authorization': 'my-auth-token'
    })
  };

  constructor(private http: HttpClient) { }

  test(): string {
    return 'working';
  }

  login(user: User): Observable<any> {
    let url: string = `${this.BASE_URL}/login`;
    return this.http.post(url, user, this.httpOptions);
  }

}
