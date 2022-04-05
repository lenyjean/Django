from rest_framework import serializers



class Messages(serializers.Serializer):
    mid = serializers.CharField(max_length=200)
    text = serializers.CharField(max_length=200)

class Sender(serializers.Serializer):
    id = serializers.CharField(max_length=255)

class Recipient(serializers.Serializer):
    id = serializers.CharField(max_length=255)

class Messenger(serializers.Serializer):
    sender = Sender
    recipient = Recipient
    timestamp = serializers.CharField(max_length=255)
    messages = Messages


class Webhooks(serializers.Serializer):
    object = serializers.CharField(max_length=255)
    entry = Messenger(many=True)

