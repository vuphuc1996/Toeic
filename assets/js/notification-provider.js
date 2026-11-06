export class LocalNotificationProvider {
  constructor(getRegistration) {
    this.getRegistration = typeof getRegistration === 'function' ? getRegistration : async () => null;
    this.kind = 'github-local';
  }
  getCapabilities() {
    return {
      kind: this.kind,
      systemNotifications: 'Notification' in window && 'serviceWorker' in navigator,
      backgroundPush: false,
      serverRequired: false,
      scheduling: 'foreground-and-return-check'
    };
  }
  async requestPermission() {
    if (!('Notification' in window)) return 'unsupported';
    return Notification.requestPermission();
  }
  async sendNotification({ title, body, url, tag = 'toeic-local-reminder' } = {}) {
    if (!('Notification' in window) || Notification.permission !== 'granted') {
      return { delivered: false, reason: 'permission-not-granted' };
    }
    const registration = await this.getRegistration();
    if (!registration?.showNotification) return { delivered: false, reason: 'service-worker-unavailable' };
    await registration.showNotification(title || 'TOEIC Dictionary', {
      body: body || 'Đã đến giờ ôn tập TOEIC.',
      icon: new URL('../../assets/icons/icon-192.png', import.meta.url).href,
      badge: new URL('../../assets/icons/icon-192.png', import.meta.url).href,
      tag,
      renotify: true,
      data: { url: url || new URL('../../?open=practice', import.meta.url).href }
    });
    return { delivered: true, channel: 'service-worker-notification' };
  }
}
