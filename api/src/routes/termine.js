import { Router } from 'express';
import db from '../db.js';

const router = Router();

export function publicTermin(row) {
  return {
    id: row.id,
    date: row.date,
    time: row.time,
    location: row.location,
    topic: row.topic,
    link: row.link,
    cancelled: !!row.cancelled,
    recurring: !!row.recurring,
    validFrom: row.valid_from,
    validUntil: row.valid_until,
  };
}

router.get('/termine', (_req, res) => {
  const rows = db.prepare('SELECT * FROM termine ORDER BY id').all();
  res.json(rows.map(publicTermin));
});

export default router;
