import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { AsyncPipe, NgFor, NgIf } from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-albums',
  imports: [CommonModule, RouterLink, NgFor, NgIf, AsyncPipe],
  templateUrl: './albums.html'
})
export class AlbumsComponent {}

