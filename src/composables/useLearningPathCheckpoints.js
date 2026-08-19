/** Week-to-topic checkpoint mapping (derived from topics.json links.weekNumbers). */
export const CHECKPOINT_TOPIC_IDS = {
  1: ['print-und-ausgabe', 'variablen'],
  3: ['bedingungen'],
};

export function getCheckpointTopicIds(weekNumber) {
  return CHECKPOINT_TOPIC_IDS[weekNumber] || [];
}

export function hasWeekCheckpoint(weekNumber) {
  return getCheckpointTopicIds(weekNumber).length > 0;
}

export function isWeekCheckpointComplete(weekNumber, isTopicDone) {
  const ids = getCheckpointTopicIds(weekNumber);
  if (!ids.length) return false;
  return ids.every((id) => isTopicDone(id));
}
