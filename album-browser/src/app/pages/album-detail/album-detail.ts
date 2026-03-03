import { Component, OnInit, NgZone, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule, RouterLink } from '@angular/router';
import { ActivatedRoute, Router } from '@angular/router';
import { AlbumService } from '../../core/services/album.service';
import { Album } from '../../core/models/album';

@Component({
  selector: 'app-album-detail',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule, RouterLink],
  template: `
    <div *ngIf="loading">Loading...</div>

    <div *ngIf="!loading">
      <h2>Album Details</h2>
      <p><strong>ID:</strong> {{ album.id }}</p>
      <p><strong>User ID:</strong> {{ album.userId }}</p>

      <label>
        Title:
        <input [(ngModel)]="album.title" />
      </label>
      <button (click)="save()">Save</button>

      <br><br>
      <button [routerLink]="['/albums', album.id, 'photos']">View Photos</button>
      <button (click)="back()">Back</button>
    </div>
  `
})
export class AlbumDetail implements OnInit {
  album!: Album;
  loading = true;

  constructor(
    private route: ActivatedRoute,
    private albumService: AlbumService,
    private router: Router,
    private ngZone: NgZone, 
    private cd: ChangeDetectorRef
  ) {}

    ngOnInit(): void {
      const id = Number(this.route.snapshot.paramMap.get('id'));
      this.albumService.getAlbum(id).subscribe({
        next: data => {
          this.ngZone.run(() => {
            this.album = data;
            this.loading = false;
            this.cd.detectChanges();
          });
        },
        error: err => {
          console.error(err);
          this.ngZone.run(() => {
            this.loading = false;
            this.cd.detectChanges();
          });
        }
      });
    }

  save() {
    this.albumService.updateAlbum(this.album).subscribe();
  }

  back() {
    this.router.navigate(['/albums']);
  }
}