import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, RouterLink, ActivatedRoute, Router } from '@angular/router';
import { AlbumService } from '../../core/services/album.service';
import { Photo } from '../../core/models/photo';

@Component({
  selector: 'app-album-photos',
  standalone: true,
  imports: [CommonModule, RouterModule, RouterLink],
  template: `
    <div *ngIf="loading">Loading photos...</div>

    <div class="grid" *ngIf="!loading && photos.length > 0">
      <div *ngFor="let photo of photos" class="photo-card">
        <img [src]="photo.thumbnailUrl" [alt]="photo.title">
        <p>{{ photo.title }}</p>
      </div>
    </div>

    <div *ngIf="!loading && photos.length === 0">
      <p>No photos found for this album.</p>
    </div>

    <button (click)="back()">Back</button>
  `,
  styleUrls: ['./album-photos.css']
})
export class AlbumPhotos implements OnInit {
  photos: Photo[] = [];
  loading = true;
  albumId!: number;

  constructor(
    private route: ActivatedRoute,
    private albumService: AlbumService,
    private router: Router
  ) {}

  ngOnInit(): void {
    const param = this.route.snapshot.paramMap.get('id');
    this.albumId = param ? Number(param) : 0;

    if (!this.albumId || isNaN(this.albumId)) {
      console.error('Invalid album ID:', param);
      this.loading = false;
      return;
    }

    this.albumService.getAlbumPhotos(this.albumId).subscribe({
      next: (p) => {
        console.log('Photos received:', p);
        this.photos = p;
        this.loading = false;
      },
      error: (err) => {
        console.error('Error fetching photos:', err);
        this.loading = false;
      }
    });
  }

  back() {
    this.router.navigate(['/albums', this.albumId]);
  }
}