from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.conversation import Conversation
from app.schemas.conversation import ConversationCreate


class ConversationNotFoundError(Exception):
    pass


async def create_conversation(
    session: AsyncSession,
    user_id: int,
    data: ConversationCreate,
) -> Conversation:
    conversation = Conversation(
        user_id=user_id,
        title=data.title,
        system_prompt=data.system_prompt,
    )

    session.add(conversation)
    await session.commit()
    await session.refresh(conversation)

    return conversation


async def list_user_conversations(
    session: AsyncSession,
    user_id: int,
) -> list[Conversation]:
    result = await session.scalars(
        select(Conversation)
        .where(Conversation.user_id == user_id)
        .order_by(Conversation.updated_at.desc())
    )

    return list(result.all())


async def get_user_conversation(
    session: AsyncSession,
    user_id: int,
    conversation_id: int,
) -> Conversation:
    conversation = await session.scalar(
        select(Conversation).where(
            Conversation.id == conversation_id,
            Conversation.user_id == user_id,
        )
    )

    if conversation is None:
        raise ConversationNotFoundError("Conversation not found")

    return conversation


async def delete_user_conversation(
    session: AsyncSession,
    user_id: int,
    conversation_id: int,
) -> None:
    result = await session.execute(
        delete(Conversation).where(
            Conversation.id == conversation_id,
            Conversation.user_id == user_id,
        )
    )

    if result.rowcount == 0:
        raise ConversationNotFoundError("Conversation not found")

    await session.commit()
