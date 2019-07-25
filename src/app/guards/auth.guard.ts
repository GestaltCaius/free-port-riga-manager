import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthService } from '../services/auth.service';
import { User } from '../services/user';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  
constructor(private authService: AuthService) {}

  canActivate(): boolean {
    // let user = new User();
    // user.email = 'toto.titi@example.com';
    // user.password = 'hello';

    // this.authService.login(user);

    // const res = this.authService.isLoggedIn().subscribe(
    //   val => console.log(val),
    //   err => console.log(err)
    // );
    return true;
  }
}``